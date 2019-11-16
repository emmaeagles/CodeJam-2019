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
          @change="onFileChanged"
        >
        <div id="results">
          <p> </p>
        </div>
        <q-btn
              color="secondary"
              class="glossy"
              @click="sendFile"
              label="UPLOAD"
        />
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'MyLayout',
  data () {
    return {
      file: null
    }
  },
  methods: {
    onFileChanged: function (event) {
      this.file = event.target.files[0]
    },
    sendFile: function (event) {
      const formData = new FormData()
      formData.append('file', this.file)
      this.$axios.post('http://localhost:5000/upload', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
    }
  }
}
</script>
