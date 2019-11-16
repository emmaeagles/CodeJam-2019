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
        <q-btn
          class="glossy"
          :ripple="{ center: true }"
          color="teal"
          label="Find Your Items"
        />
        <q-btn
          :loading="loading2"
          :percentage="percentage2"
          round
          color="secondary"
          class="glossy"
          @click="startComputing(2)"
          icon="cloud_upload"
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
      leftDrawerOpen: false
    }
  }
}
</script>
