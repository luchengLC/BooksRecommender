<template>
  <div class="mainContent" style="margin: 0; padding: 0"
       v-loading.fullscreen.lock="fullscreenLoading">
    <div class="search-bar">
      <div class="div-input">
        <el-input class="search-input" placeholder="在系统中查找..." v-model="searchInput"
                  @keyup.enter.native="backMain"></el-input>
        <el-button class="search-btn" slot="append" icon="el-icon-search"
                   @click="backMain"></el-button>
      </div>
    </div>

    <h3 class="page-title"><i class="el-icon-menu"></i>我的喜爱列表</h3>
    <el-button type="text" style="padding: 0; margin: 2px 30px 2px 2px; text-align: right" @click="changeShow">{{showText}}</el-button>
    <el-collapse v-model="activeNames">
      <el-collapse-item name="5">
        <template slot="title">
          <el-rate
            class="el-rate"
            v-model="value5"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}星">
          </el-rate>
        </template>
        <ul class="books-container">
          <li class="book-item" v-for="(item, index) in fiveStarBooks" :key="index">
            <div class="pic">
              <a target="_blank" :href="item.subjectUrl" :title="item.bookName">
                <img class="img" :src="item.imgUrl" :alt="item.bookName">
              </a>
            </div>
            <div class="info" v-if="showInfo">
              <h2 class="bname">
                <a target="_blank" class="aname" :href="item.subjectUrl">{{item.bookName}}</a>
              </h2>
              <p class="publi">{{item.author}}</p>
              <p class="publi">{{item.publisher}}</p>
              <p class="publi">{{item.pubDate}}</p>
              <p class="price">{{item.price}}</p>
              <div class="evaluate">
                <span class="score">{{item.ratingScore}}</span>
                <span class="num">（{{item.ratingNum}}人评价）</span>
              </div>
              <!--<p class="brief">简介：{{item.brief}}</p>-->
              <el-button class="remove-btn" type="primary" size="mini" @click="handleFavorRemove(item)">移除</el-button>
            </div>

          </li>
        </ul>
      </el-collapse-item>
      <el-collapse-item name="4">
        <template slot="title">
          <el-rate
            class="el-rate"
            v-model="value4"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}星">
          </el-rate>
        </template>
        <ul class="books-container">
          <li class="book-item" v-for="(item, index) in fourStarBooks" :key="index">
            <div class="pic">
              <a target="_blank" :href="item.subjectUrl" :title="item.bookName">
                <img class="img" :src="item.imgUrl" :alt="item.bookName">
              </a>
            </div>
            <div class="info" v-if="showInfo">
              <h2 class="bname">
                <a target="_blank" class="aname" :href="item.subjectUrl">{{item.bookName}}</a>
              </h2>
              <p class="publi">{{item.author}}</p>
              <p class="publi">{{item.publisher}}</p>
              <p class="publi">{{item.pubDate}}</p>
              <p class="price">{{item.price}}</p>
              <div class="evaluate">
                <span class="score">{{item.ratingScore}}</span>
                <span class="num">（{{item.ratingNum}}人评价）</span>
              </div>
              <!--<p class="brief">简介：{{item.brief}}</p>-->
              <el-button class="remove-btn" type="primary" size="mini" @click="handleFavorRemove(item)">移除</el-button>
            </div>


          </li>
        </ul>
      </el-collapse-item>
      <el-collapse-item name="3">
        <template slot="title">
          <el-rate
            class="el-rate"
            v-model="value3"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}星">
          </el-rate>
        </template>
        <ul class="books-container">
          <li class="book-item" v-for="(item, index) in threeStarBooks" :key="index">
            <div class="pic">
              <a target="_blank" :href="item.subjectUrl" :title="item.bookName">
                <img class="img" :src="item.imgUrl" :alt="item.bookName">
              </a>
            </div>
            <div class="info" v-if="showInfo">
              <h2 class="bname">
                <a target="_blank" class="aname" :href="item.subjectUrl">{{item.bookName}}</a>
              </h2>
              <p class="publi">{{item.author}}</p>
              <p class="publi">{{item.publisher}}</p>
              <p class="publi">{{item.pubDate}}</p>
              <p class="price">{{item.price}}</p>
              <div class="evaluate">
                <span class="score">{{item.ratingScore}}</span>
                <span class="num">（{{item.ratingNum}}人评价）</span>
              </div>
              <!--<p class="brief">简介：{{item.brief}}</p>-->
              <el-button class="remove-btn" type="primary" size="mini" @click="handleFavorRemove(item)">移除</el-button>
            </div>

          </li>
        </ul>
      </el-collapse-item>
      <el-collapse-item name="2">
        <template slot="title">
          <el-rate
            class="el-rate"
            v-model="value2"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}星">
          </el-rate>
        </template>
        <ul class="books-container">
          <li class="book-item" v-for="(item, index) in twoStarBooks" :key="index">
            <div class="pic">
              <a target="_blank" :href="item.subjectUrl" :title="item.bookName">
                <img class="img" :src="item.imgUrl" ::alt="item.bookName">
              </a>
            </div>
            <div class="info" v-if="showInfo">
              <h2 class="bname">
                <a target="_blank" class="aname" :href="item.subjectUrl">{{item.bookName}}</a>
              </h2>
              <p class="publi">{{item.author}}</p>
              <p class="publi">{{item.publisher}}</p>
              <p class="publi">{{item.pubDate}}</p>
              <p class="price">{{item.price}}</p>
              <div class="evaluate">
                <span class="score">{{item.ratingScore}}</span>
                <span class="num">（{{item.ratingNum}}人评价）</span>
              </div>
              <!--<p class="brief">简介：{{item.brief}}</p>-->
              <el-button class="remove-btn" type="primary" size="mini" @click="handleFavorRemove(item)">移除</el-button>
            </div>

          </li>
        </ul>
      </el-collapse-item>
      <el-collapse-item name="1">
        <template slot="title">
          <el-rate
            class="el-rate"
            v-model="value1"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}星">
          </el-rate>
        </template>
        <ul class="books-container">
          <li class="book-item" v-for="(item, index) in oneStarBooks" :key="index">
            <div class="pic">
              <a target="_blank" :href="item.subjectUrl" :title="item.bookName">
                <img class="img" :src="item.imgUrl" :alt="item.bookName">
              </a>
            </div>
            <div class="info" v-if="showInfo">
              <h2 class="bname">
                <a target="_blank" class="aname" :href="item.subjectUrl">{{item.bookName}}</a>
              </h2>
              <p class="publi">{{item.author}}</p>
              <p class="publi">{{item.publisher}}</p>
              <p class="publi">{{item.pubDate}}</p>
              <p class="price">{{item.price}}</p>
              <div class="evaluate">
                <span class="score">{{item.ratingScore}}</span>
                <span class="num">（{{item.ratingNum}}人评价）</span>
              </div>
              <!--<p class="brief">简介：{{item.summary}}</p>-->

              <el-button class="remove-btn" type="primary" size="mini" @click="handleFavorRemove(item)">移除</el-button>
            </div>
          </li>
        </ul>
      </el-collapse-item>
    </el-collapse>

    <div style="margin: 50px 0 20px 0; padding: 0;">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="1000">
      </el-pagination>
    </div>

  </div>
</template>

<script>
  import ElButton from '../../../../node_modules/element-ui/packages/button/src/button'
  export default {
    components: {ElButton},
    data () {
      return {
        userId: '', // 缓存topBar 传过来的userId
        fullscreenLoading: false,
        baseUrl: 'http://127.0.0.1:8000/recommend/',
        searchInput: '',
        value5: 5,
        value4: 4,
        value3: 3,
        value2: 2,
        value1: 1,
        activeNames: '5',
        showInfo: true,  // 是否显示详细信息
        fiveStarBooks: [],
        fourStarBooks: [],
        threeStarBooks: [],
        twoStarBooks: [],
        oneStarBooks: [],
        showText: '简版显示',
        searchState: 0,  // 表示没有使用search功能
      }
    },
    mounted: function () {
      this.$nextTick(function () {
        this.showText = '简版显示';
        this.showInfo = true;
        this.searchState = 0;
        this.init()
        // 请求
      })
    },

    watch: {
      '$route'(to, from){
        if (to.name === 'favor' && from.name === 'main') {
          this.showText = '简版显示';
          this.showInfo = true;
          this.searchState = 0;
          this.init();
        }
      }
    },
    methods: {
      init() {
        this.fullscreenLoading = true;
        this.userId = this.$route.params.userId;
        this.handleGetFavor();
      },
      handleGetFavor() {
        let params = new URLSearchParams();
        params.append('userId', this.userId);
        let url = this.baseUrl + 'favor/query';
        let _this = this;
        this.$axios(
          {
            method: 'post',
            url: url,
            data: params,
          }
        )
          .then((response) => {
            let res = response.data;
            console.log(res)

            if (res['error_code'] === 0) {
              _this.fiveStarBooks = res['data']['list']['star_5'];
              _this.fourStarBooks = res['data']['list']['star_4'];
              _this.threeStarBooks = res['data']['list']['star_3'];
              _this.twoStarBooks = res['data']['list']['star_2'];
              _this.oneStarBooks = res['data']['list']['star_1'];

              _this.$message.success(res['msg'])
            } else {
              _this.$message.error(res['msg']);
            }
            this.fullscreenLoading = false;
          })
          .catch(function (err) {
            console.log('favor list query error === ' + err);
            _this.$message.error('获取喜爱列表操作异常！请重试！');
          });
      },
      handleFavorRemove(item) {
        let params = new URLSearchParams();
        params.append('userId', this.userId);
        params.append('bookId', item.bookId);
        let url = this.baseUrl + 'favor/delete';
        let _this = this;
        this.$axios(
          {
            method: 'post',
            url: url,
            data: params,
          }
        )
          .then((response) => {
            let res = response.data;
            console.log(res)
            if (res['error_code'] === 0) {
              this.handleGetFavor();
              _this.$message.success(res['msg'])
            } else {
              _this.$message.error(res['msg']);
            }
          })
          .catch(function (err) {
            console.log('favor list delete error === ' + err);
            _this.$message.error('移除操作异常！请重试！');
          });
      },
      changeShow(){
        if (this.showInfo === true) {  // 非简版的状态
          this.showInfo = false;
          this.showText = '详细显示';
        } else {
          this.showInfo = true;
          this.showText = '简版显示';
        }
      },
      backMain() {
        this.searchState = 1;
        if (this.searchInput === '') {
          this.$message.error('请输入搜索内容！')

        } else {
          this.$router.push({
            name: 'main',
            params: {
              userId: this.userId,
              searchInput: this.searchInput,
              searchState: this.searchState,
            }
          });
          this.searchInput = '';
          this.searchState = 0;
        }

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
    width: 100%;
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

    .el-rate {
      padding-top: 15px;
    }

    .books-container {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: row; /* 方向 横   */
      flex-wrap: wrap; /* 换行 */
      margin: 24px 40px 5px 5px;
      /*justify-content: center;*/
      width: 100%;
      .book-item {
        min-width: 110px;
        border-top: 1px dashed #ddd;
        margin: 10px 10px 20px 10px;
        padding: 10px 0 0 0;
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        flex-direction: row;

        .pic {
          float: left;
          margin-right: 20px;
          width: 105px;
          height: 160px;
          .a {
            color: #3377aa;
            text-decoration: none;
          }
          img {
            min-width: 100px;
            min-height: 145px;
            max-width: 110px;
            max-height: 160px;
          }

        }
        .info {
          width: 180px;
          text-align: left;
          display: -webkit-flex; /* Safari  chrome */
          display: flex;
          flex: 1;
          flex-direction: column; /* 方向 竖   上到下*/
          flex-wrap: nowrap; /* 不换行 */
          align-items: flex-start;
          .bname {
            font-size: 14px;
            margin: 0 0 2px 0;
            .aname {
              color: #3377aa;
              text-decoration: none;
            }
          }
          .publi {
            font-size: 13px;
            margin: 1px 0 1px;
            color: #666;
            text-align: -webkit-match-parent;
          }
          .price {
            font-size: 15px;
            font-weight: 600;
            margin: 1px 0 1px;
            color: #ee8080;
            text-align: -webkit-match-parent;
          }
          .evaluate {
            font-size: 14px;
            margin: 1px 0 1px;
            color: #666;
            text-align: left;
            .score {
              color: #e09015;
              font-weight: 800;
            }
          }
          .brief {
            display: block;
            -webkit-margin-before: 1em;
            -webkit-margin-after: 1em;
            -webkit-margin-start: 0px;
            -webkit-margin-end: 0px;
            font-size: 14px;
            margin: 0px 0 0px;
            color: #666;
            text-align: left;
          }

        }
        .remove-btn {
          align-self: flex-end;
        }
      }
    }
  }

</style>
