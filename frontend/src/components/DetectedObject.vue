<template>
<div>
  <q-checkbox v-model="checked"></q-checkbox>
    <q-card style="min-width: 750px; margin: 20px;">
      <q-card-section class="bg-white text-black">
        <div class="text-h6">Object: {{ object }}</div>
        <p>Link: {{ link }}</p>
        <p>Percentage Certainty: {{ percentageCertainty }}%</p>
      </q-card-section>

      <q-card-actions align="left">
        <q-btn flat>Remove</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'DetectedObject',
  props: {
    link: String,
    object: String,
    percentageCertainty: Number
  }
}
</script>
