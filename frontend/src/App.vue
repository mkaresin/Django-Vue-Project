<template>
  <div id="app">
    
    <maincomponent />


  </div>
</template>



<script>
import maincomponent from './components/maincomponent.vue'


export default {
  name: 'app',
  components: {
    maincomponent
  }
 
}
</script>



<style>
@import'~bootstrap/dist/css/bootstrap.css'

</style>
