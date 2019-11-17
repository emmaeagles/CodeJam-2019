<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-white text-blue">
        <q-toolbar-title>
          <strong>HIPA - Home Insurance Photo Analyzer</strong>
        </q-toolbar-title>
        <div>CodeJam 2019</div>
      </q-toolbar>
    </q-header>

    <q-page id="background">
      <q-page-container>
        <q-page class="flex column flex-center">
          <q-card
            style="padding: 25px; width: 900px; margin: 50px"
            class="flex column flex-center"
          >
            <input
              type="file"
              style="margin-top: 50px; margin-bottom: 20px"
              @change="onFileChanged"
            >
            <q-btn
              Updated
              upstream
              color="secondary"
              class="glossy"
              @click="sendFile"
              label="UPLOAD"
            />
            <div>
              <p> </p>
            </div>
            <div v-if="isLoading==true">
              <component
                :is="`q-spinner-hourglass`"
                color='secondary'
                size='36px'
              />
            </div>
            <div>
              <p> </p>
            </div>
            <div v-if="resultFetched==true">
              <p style="text-align: center; margin-top: 20px">
                <img
                  width="600"
                  v-bind:src="'data:image/jpg;base64,' + encoded_file"
                >
              </p>

              <DetectedObject
                v-for="result in response_result"
                v-bind:key="result.id"
                :price="result.price"
                :id="result.id"
                :link='result.link'
                :object='result.name'
                v-bind:percentageCertainty='parseInt(result.percentageCertainty)'
                @child-checkbox='handleChecked'
              ></DetectedObject>
              <p>
                Total: {{ total_amount }}
              </p>
            </div>
          </q-card>
        </q-page>
      </q-page-container>
    </q-page>
  </q-layout>
</template>

<script>
import DetectedObject from '../components/DetectedObject.vue'

let remove = function (context, object) {
  for (var i = 0; i < context.selected_objects.length; i++) {
    if (context.selected_objects[i].id === object.id) {
      context.selected_objects.splice(i, 1)
    }
  }
}

export default {
  name: 'MyLayout',
  components: {
    DetectedObject
  },
  data () {
    return {
      file: null,
      isLoading: false,
      resultFetched: false,
      response_result: [],
      encoded_file: '',
      selected_objects: [],
      total_amount: 0
    }
  },
  methods: {
    onFileChanged: function (event) {
      this.file = event.target.files[0]
      this.response_result = []
      this.selected_objects = []
      this.total = 0
    },
    sendFile: function (event) {
      this.total = 0
      this.response_result = []
      this.selected_objects = []
      this.isLoading = true
      const formData = new FormData()
      formData.append('file', this.file)
      this.$axios.post('http://localhost:5000/upload', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
        .then(resp => {
          this.isLoading = false
          this.resultFetched = true
          this.encoded_file = resp.data.file_encoded
          console.log(resp.data.result)
          for (let i = 0; i < resp.data.result.length; i++) {
            console.log('HERE')
            this.response_result.push({ name: resp.data.result[i].metadata.name, link: resp.data.result[i].link, percentageCertainty: resp.data.result[i].metadata.percentage_probability, price: resp.data.result[i].price, id: i + 1 })
            this.selected_objects.push({ name: resp.data.result[i].metadata.name, link: resp.data.result[i].link, percentageCertainty: resp.data.result[i].metadata.percentage_probability, price: resp.data.result[i].price, id: i + 1 })
          }
        })
        .catch(error => {
          console.log(error.resp)
          this.isLoading = false
        })
    },
    handleChecked: function (isChecked, object) {
      // Adds a profile to the selected list if their box is checked
      if (isChecked) {
        this.selected_objects.push(object)
        this.total_amount += parseFloat(object.price).toFixed(2)
      } else {
        remove(this, object)
        this.total_amount -= parseFloat(object.price).toFixed(2)
      }
      console.log(this.selected_objects)
    }
  }
}
</script>

<style scoped>
#whiteCard {
  background-image: url("../assets/background.jpeg");
  align-content: center;
}
</style>
