<template>
  <div style="margin: 0; padding: 0;">
    <mainContent class="mainContent"></mainContent>
    <hotContent class="hotContent"></hotContent>
    <!--<myFavor class="myFavor"></myFavor>-->
    <!--<pagers class="pagers"></pagers>-->
  </div>
</template>

<script>
import MainContent from './mid/MainContent'
import HotContent from './mid/HotContent'
import MyFavor from './mid/MyFavor'
import Pagers from './Pagers'
export default {
  components: {
    'mainContent': MainContent,
    'hotContent': HotContent,
    'myFavor': MyFavor,
    'pagers': Pagers
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .mainContent {
  }
  .hotContent {
    display: none;
  }
  .myFavor {
    display: none;
  }
</style>
