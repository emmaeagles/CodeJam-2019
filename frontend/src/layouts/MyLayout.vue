<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          HIPA - Home Insurance Photo Analyzer
        </q-toolbar-title>
        <div>CodeJam 2019</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <q-page class="flex column flex-center">
        <input
          type="file"
          style="margin-top: 50px"
          @change="onFileChanged"
        >
        <div>
          <p> </p>
        </div>
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
        <q-btn
          color="secondary"
          class="glossy"
          @click="sendFile"
          label="Evaluate"
        />
        <div v-if="resultFetched==true">
          <p style="text-align: center; margin-top: 20px">
            <img width="700" v-bind:src="'data:image/jpg;base64,' + response_result.file_encoded">
          </p>
          <DetectedObject
            v-for="result in response_result.result"
            v-bind:key="result.id"
            :id="result.id"
            :link='result.link'
            :object='result.name'
            v-bind:percentageCertainty='parseInt(result.percentageCertainty)'
            @child-checkbox='handleChecked'
          ></DetectedObject>
        </div>
      </q-page>
    </q-page-container>
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
      selected_objects: []
    }
  },
  methods: {
    onFileChanged: function (event) {
      this.file = event.target.files[0]
    },
    sendFile: function (event) {
      this.isLoading = true
      const formData = new FormData()
      formData.append('file', this.file)
      this.$axios.post('http://localhost:5000/upload', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
        .then(resp => {
          this.isLoading = false
          this.resultFetched = true
          // this.response_result = resp.data
          // this.selected_objects = resp.data
          console.log(resp.data)
          for (let i = 0; i < resp.data.length; i++) {
            console.log('HERE')
            this.response_result.push({ name: resp.data[i].metadata.name, link: resp.data[i].link, percentageCertainty: resp.data[i].metadata.percentage_probability, id: i + 1 })
            this.selected_objects.push({ name: resp.data[i].metadata.name, link: resp.data[i].link, percentageCertainty: resp.data[i].metadata.percentage_probability, id: i + 1 })
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
      } else {
        remove(this, object)
      }
      console.log(this.selected_objects)
    }
  }
}
</script>
