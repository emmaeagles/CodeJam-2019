<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          Smash
        </q-toolbar-title>
        <div>CodeJam 2019</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <q-page class="flex flex-center">
        <div>
          <q-btn class="glossy" :ripple="{ center: true }" color="teal" label="GENERATE" />
        </div>

        <div class="row">
            <q-btn
              :loading="loading2"
              :percentage="percentage2"
              round
              color="secondary"
              class="glossy"
              @click="startComputing(2)"
              icon="cloud_upload"
            />
          <div class="col-6 items-center"><q-btn
              :loading="loading2"
              :percentage="percentage2"
              round
              color="secondary"
              class="glossy"
              @click="startComputing(2)"
              icon="cloud_upload"
            /></div>
        </div>
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
