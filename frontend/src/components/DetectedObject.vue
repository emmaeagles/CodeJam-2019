<template>
  <div>
    <q-card style="min-width: 750px; margin: 20px;">
      <q-card-section class="bg-white text-black">
        <div class="text-h6">Object: {{ object }}</div>
        <p>Link: <a
            :href='link'
            target="_blank"
          >{{ link }}</a></p>
        <p>Percentage Certainty: {{ percentageCertainty }}%</p>
        <p>Price: ${{ price }}</p>
        <q-checkbox
          keep-color
          v-model="checked"
          color="teal"
          @input="handleChecked"
        />
      </q-card-section>

      <q-card-actions align="left">
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'DetectedObject',
  data () {
    return { teal: true, obj_id: this.id, checked: true }
  },
  props: {
    link: String,
    object: String,
    percentageCertainty: Number,
    price: String,
    id: Number
  },
  methods: {
    handleChecked: function () {
      this.$emit('child-checkbox', this.checked, { name: this.object, link: this.link, percentageCertainty: this.percentageCertainty, price: this.price, id: this.obj_id })
    }
  }
}
</script>
