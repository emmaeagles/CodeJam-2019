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
      <q-page class="flex flex-center">
        <input
          type="file"
          @change="onFileChanged"
        >
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'MyLayout',
  data () {
    return {
    }
  },
  methods: {
    onFileChanged: function (event) {
      const file = event.target.files[0]
      const formData = new FormData()
      formData.append('file', file)
      this.$axios.post('http://localhost:5000/upload', file, { headers: { 'Content-Type': 'multipart/form-data' } })
    }
  }
}
</script>
