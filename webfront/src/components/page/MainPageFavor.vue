<template>
  <div class="main" style="margin: 0; padding: 0">
    <top-bar class="top-bar"></top-bar>
    <div class="mid-parent">
      <div class="mid">  <!--去掉-->
        <contentFavor class="contentFavor"></contentFavor>
      </div>
    </div>
    <bottom class="bottom"></bottom>
  </div>
</template>

<script>
  import TopBar from './parts/TopBar'
  import ContentFavor from './parts/ContentFavor'
  import Bottom from './parts/Bottom'

  export default {
    components: {
      'topBar': TopBar,
      'contentFavor': ContentFavor,
      'bottom': Bottom
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .main {
    display: -webkit-flex; /* Safari  chrome */
    display: flex;
    flex-direction: column; /* 方向 列   上到下*/
    .mid-parent {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: column; /* 方向 列   上到下*/
      align-items: center;
      background: #f5f5f5;
      .mid {
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        flex-direction: row; /* 方向 横   左到右*/
        flex-wrap: nowrap; /* 不许换行 */
        justify-content: center;
        width: 90%;
        .midBig {
          display: -webkit-flex; /* Safari  chrome */
          display: flex;
          flex-direction: row; /* 方向 树   上到下*/
          .contentFavor {

          }
        }
      }
    }
    .bottom {
      background: #fff;
    }
  }

</style>
