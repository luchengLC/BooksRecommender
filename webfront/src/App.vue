<!--<template>-->
  <!--<div id="app">-->
    <!--<img src="./assets/logo.png">-->
    <!--<router-view/>-->
  <!--</div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
  <!--name: 'App'-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
  <!--font-family: 'Avenir', Helvetica, Arial, sans-serif;-->
  <!-- -webkit-font-smoothing: antialiased;-->
  <!-- -moz-osx-font-smoothing: grayscale;-->
  <!--text-align: center;-->
  <!--color: #2c3e50;-->
  <!--margin-top: 60px;-->
<!--}-->
<!--</style>-->

<template>
  <div id="app">
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
  export default {
    urlHeader: 'http://127.0.0.1:8000/bookRecommender/',
    name: 'App'
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  body {
    margin: 0;
    min-width: 430px;
    min-width: 535px;
  }
</style>
