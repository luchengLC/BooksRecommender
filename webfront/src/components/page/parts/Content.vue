<template>
  <div style="margin: 0; padding: 0;">
    <div class="mainContent" style="margin: 0; padding: 0">
      <div class="search-bar">
        <div class="div-input">
          <el-input class="search-input" placeholder="搜索..." v-model="searchInput"></el-input>
          <el-button class="search-btn" slot="append" icon="el-icon-search" @click="searchHandle"></el-button>
        </div>
      </div>

      <h3 class="page-title" v-if="showInitHot"><i class="el-icon-menu"></i>热门</h3>
      <ul class="books-hot" v-if="showInitHot">
        <li class="book-item" v-for="(item, index) in hotBooks" :key="index">
          <div class="pic">
            <a target="_blank" class="a" :href="item.bookLink">
              <img class="img" :src="item.imgUrl" alt=""/>
            </a>
          </div>
          <div class="info">
            <div class="title">
              <a target="_blank" class="a" :href="item.bookLink">
                {{item.bname}}
              </a>
            </div>
            <div class="author">
              {{item.author}}
            </div>
          </div>
        </li>
      </ul>
      <!--搜索 结果 书表-->
      <h3 class="page-title" v-if="showSearchResult"><i class="el-icon-menu"></i>搜索结果</h3>
      <ul class="books-container"  v-if="showSearchResult">
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
      <div class="page" v-if="showSearchResult">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="1000">
        </el-pagination>
      </div>
    </div>





    <!--右侧-->
    <div class="hotContent" v-if="showSearchResult">
      <div style="margin: 50px 0 0 0; padding: 0">
        <!--标签推荐-->
        <h3 class="right-page-title"><i class="el-icon-menu"></i>标签推荐</h3>
        <div class="tags">
          <el-button class="tag-btn" type="text" v-for="(item, index) in tags">
            <el-tag class="tag">{{item.tagName}}</el-tag>
          </el-button>
        </div>

        <!--书籍推荐-->
        <h3 class="right-page-title"><i class="el-icon-menu"></i>书籍推荐</h3>
        <ul class="books-recommend">
          <li class="book-item" v-for="(item, index) in bookRec" :key="index">
            <div class="pic">
              <a target="_blank" class="a" :href="item.bookLink">
                <img class="img" :src="item.imgUrl" alt=""/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a target="_blank" class="a" :href="item.bookLink">
                  {{item.bname}}
                </a>
              </div>
              <div class="author">
                {{item.author}}
              </div>
            </div>
          </li>
        </ul>


        <h3 class="right-page-title"><i class="el-icon-menu"></i>HOT</h3>
        <ul class="books-hot">
          <li class="book-item" v-for="(item, index) in hotBooks" :key="index">
            <div class="pic">
              <a target="_blank" class="a" :href="item.bookLink">
                <img class="img" :src="item.imgUrl" alt=""/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a target="_blank" class="a" :href="item.bookLink">
                  {{item.bname}}
                </a>
              </div>
              <div class="author">
                {{item.author}}
              </div>
            </div>
          </li>
        </ul>
      </div>


    </div>
  </div>
</template>

<script>
  import ElButton from '../../../../node_modules/element-ui/packages/button/src/button'
  export default {
    components: {ElButton},
    data () {
      return {
        showSearchResult: false,
        showInitHot: true,
        searchInput: '',
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
        ],
        tags: [
          {
            tagName: '文学',
          },
          {
            tagName: '政治',
          },
          {
            tagName: '心理学',
          },
          {
            tagName: '编程',
          },
          {
            tagName: '文学',
          },
          {
            tagName: '政治',
          },
          {
            tagName: '心理学',
          },
          {
            tagName: '编程',
          }
        ],
        hotBooks: [
          {
            bname: '神迹',
            bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
            imgUrl: 'https://img1.doubanio.com/mpic/s29708619.jpg',
            author: '[爱尔兰] 爱玛·多诺霍'
          },
          {
            bname: '啊！这样就能辞职了',
            bookLink: 'https://book.douban.com/subject/27201290/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/mpic/s29669694.jpg',
            author: '[日] 安倍夜郎'
          },
          {
            bname: '蟹之进行曲1',
            bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
            imgUrl: 'https://img3.doubanio.com/mpic/s29517015.jpg',
            author: '[法] 阿尔蒂尔·德·潘'
          },

          {
            bname: '植物花卉插画图案集',
            bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/mpic/s29708071.jpg',
            author: '[英] 鲍伊风尚'
          },
          {
            bname: '神迹',
            bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
            imgUrl: 'https://img1.doubanio.com/mpic/s29708619.jpg',
            author: '[爱尔兰] 爱玛·多诺霍'
          },
          {
            bname: '啊！这样就能辞职了',
            bookLink: 'https://book.douban.com/subject/27201290/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/mpic/s29669694.jpg',
            author: '[日] 安倍夜郎'
          },
          {
            bname: '蟹之进行曲1',
            bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
            imgUrl: 'https://img3.doubanio.com/mpic/s29517015.jpg',
            author: '[法] 阿尔蒂尔·德·潘'
          },

          {
            bname: '植物花卉插画图案集',
            bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/mpic/s29708071.jpg',
            author: '[英] 鲍伊风尚'
          },
          {
            bname: '神迹',
            bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
            imgUrl: 'https://img1.doubanio.com/mpic/s29708619.jpg',
            author: '[爱尔兰] 爱玛·多诺霍'
          },
          {
            bname: '啊！这样就能辞职了',
            bookLink: 'https://book.douban.com/subject/27201290/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/mpic/s29669694.jpg',
            author: '[日] 安倍夜郎'
          },
          {
            bname: '蟹之进行曲1',
            bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
            imgUrl: 'https://img3.doubanio.com/mpic/s29517015.jpg',
            author: '[法] 阿尔蒂尔·德·潘'
          },

          {
            bname: '植物花卉插画图案集',
            bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/mpic/s29708071.jpg',
            author: '[英] 鲍伊风尚'
          },

        ],
        bookRec: [
          {
            bname: '神迹',
            bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
            imgUrl: 'https://img1.doubanio.com/spic/s29708619.jpg',
            author: '[爱尔兰] 爱玛·多诺霍'
          },
          {
            bname: '植物花卉插画图案集',
            bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/spic/s29708071.jpg',
            author: '[英] 鲍伊风尚'
          },
          {
            bname: '蟹之进行曲1',
            bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
            imgUrl: 'https://img3.doubanio.com/spic/s29517015.jpg',
            author: '[法] 阿尔蒂尔·德·潘'
          },
          {
            bname: '植物花卉插画图案集',
            bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
            imgUrl: 'https://img3.doubanio.com/spic/s29708071.jpg',
            author: '[英] 鲍伊风尚'
          },
          {
            bname: '蟹之进行曲1',
            bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
            imgUrl: 'https://img3.doubanio.com/spic/s29517015.jpg',
            author: '[法] 阿尔蒂尔·德·潘'
          },
        ]
      }
    },
    mounted: function () {
      this.$nextTick(function () {
          this.showSearchResult = false;
          this.showInitHot = true;
      })
    },
    methods: {
      searchHandle(){
        this.showSearchResult = true;
        this.showInitHot = false;
      }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .mainContent {
    display: -webkit-flex; /* Safari  chrome */
    display: flex;
    flex-direction: column; /* 方向 树   上到下*/

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

    .page-title {
      color: #F56C6C;
      text-align: left;
      padding-top: 5px;
      border-top: 1px solid #ddd;
      margin-top: 30px;
      .el-icon-menu {
        margin-right: 10px;
      }
    }

    .books-hot {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: row; /* 方向 横   左到右*/
      flex-wrap: wrap; /* 换行 */
      margin: 5px 5px 0 5px;
      color: #666;
      .book-item {
        text-align: left;
        margin-bottom: 15px;
        .pic {
          width: 105px;
          height: 160px;
          .a {
            color: #3377aa;
            text-decoration: none;
            .img {
              max-height: 160px;
              max-width: 105px;
            }
          }
        }
        .info {
          .title {
            width: 105px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            .a {
              width: 105px;
              white-space: nowrap;
              overflow: hidden;
              text-overflow: ellipsis;

              color: #3377aa;
              text-decoration: none;
            }
          }
          .author {
            width: 105px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
          }
        }
      }
    }

    .books-container {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: column; /* 方向 竖   上到下*/
      flex-wrap: nowrap; /* 不换行 */
      margin: 0 5px 0 5px;
      /*justify-content: center;*/
      .book-item {
        border-bottom: 1px dashed #dde;
        margin: 10px 10px 0 10px;
        padding: 10px 0 20px 0;
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        flex-direction: row;
        .pic {
          float: left;
          margin-right: 20px;
          img {
            max-width: 110px;
            max-height: 160px;
          }
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
              text-decoration: none;
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


    .page {
      margin: 50px 0 20px 0;
      padding: 0;
    }
  }

  .hotContent {
    max-width: 500px;
    min-width: 130px;
    /*display: none;*/
    /*flex: 2;*/
    /*-webkit-box-shadow: #777 0 0 2px;*/
    /*-moz-box-shadow: #777 0 0 2px;*/
    /*box-shadow: #777 0 0 2px;*/

    margin: 20px 0 0 50px;
    .right-page-title {
      color: #F56C6C;
      text-align: left;
      font-weight: bold;
      padding-bottom: 3px;
      margin-bottom: 16px;
      margin-left: 15px;
      border-bottom: 1px solid #ddd;
      .el-icon-menu {
        margin-right: 10px;
      }
    }

    .tags {
      margin-left: 15px;
      margin-bottom: 20px;
      text-align: left;
      .tag-btn {
        padding-top: 2px;
        padding-bottom: 2px;
      }
    }

    .books-hot, .books-recommend {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: row; /* 方向 横   左到右*/
      flex-wrap: wrap; /* 换行 */
      margin: 5px 5px 0 5px;
      font-size: 12px;
      color: #666;
      .book-item {
        text-align: left;
        margin-bottom: 5px;
        .pic {
          width: 70px;
          height: 100px;
          .a {
            color: #3377aa;
            text-decoration: none;
            .img {
              max-height: 100px;
              max-width: 70px;
            }
          }
        }
        .info {
          .title {
            width: 70px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            .a {
              width: 70px;
              white-space: nowrap;
              overflow: hidden;
              text-overflow: ellipsis;

              color: #3377aa;
              text-decoration: none;
            }
          }
          .author {
            width: 70px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
          }
        }
      }
    }
  }

</style>
