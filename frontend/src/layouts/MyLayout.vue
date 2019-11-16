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
            :link='result.link'
            :object='result.metadata.name'
            v-bind:percentageCertainty='parseInt(result.metadata.percentage_probability)'
          ></DetectedObject>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import DetectedObject from '../components/DetectedObject.vue'
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
      response_result: []
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
          this.response_result = resp.data
          for (let i = 1; i <= resp.data.length; i++) {
            this.response_result[i]['id'] = i
          }
        })
        .catch(error => {
          console.log(error.resp)
          this.isLoading = false
        })
    }
  }
}
</script>
