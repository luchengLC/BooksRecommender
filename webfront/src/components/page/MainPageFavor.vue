<template>
  <div class="main" style="margin: 0; padding: 0">
    <top-bar class="top-bar"></top-bar>
    <div class="mid-parent">
      <div class="mid">  <!--去掉-->
        <midContent class="midContent"></midContent>
        <!--<rightContent class="rightContent"></rightContent>-->
      </div>
    </div>
    <bottom class="bottom"></bottom>
  </div>
</template>

<script>
  import TopBar from './parts/TopBar'
  import MidContent from './parts/ContentFavor'
  import Bottom from './parts/Bottom'

  export default {
    components: {
      'topBar': TopBar,
      'midContent': MidContent,
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
    .top-bar {
      .el-menu {
        .el-menu-item {
          height: 30px;
          line-height: 30px;
        }

        #name-login, #logout {
          float: right;
        }

        #logout {
          /*display: none;*/
        }
      }
    }
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
        width: 80%;
        .midBig {
          display: -webkit-flex; /* Safari  chrome */
          display: flex;
          flex-direction: row; /* 方向 树   上到下*/
          /*flex-wrap: wrap;  !* 要换行 *!*/
          /*flex: 4;*/
          /*-webkit-box-shadow: #777 0 0 2px;*/
          /*-moz-box-shadow: #777 0 0 2px;*/
          /*box-shadow: #777 0 0 2px;*/
          .mainContent {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
            flex-direction: column; /* 方向 树   上到下*/
            .search-bar {
              /*display: none;*/
            }
          }
          .hotContent {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
          }
          .myFavor {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
          }
        }
        .rightSmall {
          max-width: 500px;
          min-width: 130px;
          /*display: none;*/
          /*flex: 2;*/
          /*-webkit-box-shadow: #777 0 0 2px;*/
          /*-moz-box-shadow: #777 0 0 2px;*/
          /*box-shadow: #777 0 0 2px;*/
        }
      }
    }
    .bottom {
      background: #fff;
    }
  }

</style>
