<template>
  <div id="app">
    <nav_bar></nav_bar>
    <router-view></router-view>    
    <Main_footer></Main_footer>
  </div>
</template>

<script>
import footer from './components/include/footer.vue'
import nav_bar from './components/include/nav_bar.vue'

export default {
  name: 'App',
  components: {
    'Main_footer': footer,
    'nav_bar': nav_bar
  }
}
</script>

<style>

</style>
