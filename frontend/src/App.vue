<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<style>
  body {
    background-image: url('assets/background.jpeg');
    top:0px;
    left:0px;
    width: 100%;
    height: 100%;
    background-repeat: no-repeat;
    background-size: cover;
    position: absolute;
  }
</style>

<script>
export default {
  name: 'App'
}
</script>
