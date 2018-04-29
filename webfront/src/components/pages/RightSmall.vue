<template>
  <div style="margin: 0 0 20px 0;  padding: 0">
    <smallHot class="smallHot"></smallHot>
  </div>
</template>

<script>
import SmallHot from './right/SmallHot'

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'smallHot': SmallHot
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .smallHot {
  }
</style>
