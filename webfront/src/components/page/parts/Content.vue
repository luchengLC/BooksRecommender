<template>
  <div style="margin: 0; padding: 0;">
    <div class="mainContent" style="margin: 0; padding: 0">
      <div class="search-bar">
        <div class="div-input">
          <el-input class="search-input" placeholder="搜索..." v-model="input5"></el-input>
          <el-button class="search-btn" slot="append" icon="el-icon-search"></el-button>
        </div>
      </div>
      <!--书表-->
      <ul class="books-container">
        <li class="book-item" v-for="(item, index) in books" :key="index">
          <div class="pic">
            <a target="_blank" :href="item.bookLink" :title="item.bname">
              <img :src="item.imgUrl" alt="">
            </a>
          </div>
          <div class="info">
            <h2 class="bname">
              <a target="_blank" class="aname" :href="item.bookLink">{{item.bname}}</a>
            </h2>
            <p class="publi">{{item.publi}}</p>
            <div class="evaluate">
              <span>评分：</span>
              <span class="score">{{item.score}}</span>
              <span class="num">（{{item.num}}人评价）</span>
            </div>
            <p class="brief">{{item.brief}}</p>
          </div>

        </li>
      </ul>
      <!---->
      <!--分页，翻页器-->
      <div style="margin: 50px 0 20px 0; padding: 0;">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="1000">
        </el-pagination>
      </div>
    </div>


    <hotContent class="hotContent"></hotContent>
    <!--<myFavor class="myFavor"></myFavor>-->
    <!--<pagers class="pagers"></pagers>-->
  </div>
</template>

<script>
  import ElButton from '../../../../node_modules/element-ui/packages/button/src/button'
  export default {
    components: {ElButton},
    data () {
      return {
        input5: '',
        books: [
          {
            bname: '海贼王:ONE PIECE',
            publi: '尾田荣一郎 / 董科 / 浙江人民美术出版社 / 2007-11 / 7.50元',
            score: '9.5',
            num: '26534',
            brief: '路飞所生长的小村庄里曾经是一群以「红发香克斯」为首的海盗们的暂居地，而幼年路飞一直希望可以成为他们的一员，可在一次意外的情况下，他吃了一种叫做「橡皮果实」的...',
            imgUrl: 'https://img1.doubanio.com/mpic/s1492518.jpg',
            bookLink: 'https://book.douban.com/subject/1474773/'
          },
          {
            bname: '追风筝的人',
            publi: '[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元',
            score: '8.9',
            num: '308764',
            brief: '12岁的阿富汗富家少爷阿米尔与仆人哈桑情同手足。然而，在一场风筝比赛后，发生了一件悲惨不堪的事，阿米尔为自己的懦弱感到自责和痛苦，逼走了哈桑，不久，自己也跟... ',
            imgUrl: 'https://img3.doubanio.com/mpic/s1727290.jpg',
            bookLink: 'https://book.douban.com/subject/1770782/'
          },
          {
            bname: '海贼王 : ONE PIECE',
            publi: '刘慈欣 / 重庆出版社 / 2010-11 / 38.00元',
            score: '9.2',
            num: '96472',
            brief: '与三体文明的战争使人类第一次看到了宇宙黑暗的真相，地球文明像一个恐惧的孩子，熄灭了寻友的篝火，在暗夜中发抖。自以为历经沧桑，其实刚刚蹒跚学步；自以为悟出了生...',
            imgUrl: 'https://img3.doubanio.com/mpic/s26012674.jpg',
            bookLink: 'https://book.douban.com/subject/5363767/'
          }
        ]
      }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .mainContent {
    .search-bar {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      justify-content: center;
      .div-input {
        margin: 15px 0 15px 0;
        width: 400px;
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        flex-direction: row;
        .search-input {
        }
        .search-btn {
        }
      }
    }
    .books-container {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: column; /* 方向 竖   上到下*/
      flex-wrap: nowrap; /* 不换行 */
      margin: 24px 40px 5px 5px;
      /*justify-content: center;*/
      .book-item {
        border-top: 1px dashed #ddd;
        margin: 2px 10px 20px 10px;
        padding: 10px 0 0 0;
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        flex-direction: row;
        .pic {
          float: left;
          margin-right: 20px;
        }
        .info {
          display: -webkit-flex; /* Safari  chrome */
          display: flex;
          flex-direction: column; /* 方向 竖   上到下*/
          flex-wrap: nowrap; /* 不换行 */
          align-items: flex-start;
          .bname {
            font-size: 14px;
            margin: 0 0 5px 0;
            .aname {
              color: #3377aa;
              text-decoration:none;
            }
          }
          .publi {
            font-size: 14px;
            margin: 6px 0 8px;
            color: #666;
            text-align: -webkit-match-parent;
          }
          .evaluate {
            font-size: 14px;
            margin: 6px 0 8px;
            color: #666;
            text-align: left;
            .score {
              color: #e09015;
            }
          }
          .brief {
            display: block;
            -webkit-margin-before: 1em;
            -webkit-margin-after: 1em;
            -webkit-margin-start: 0px;
            -webkit-margin-end: 0px;
            font-size: 14px;
            margin: 6px 0 8px;
            color: #666;
            text-align: left;
          }
        }
      }
    }
  }

</style>
