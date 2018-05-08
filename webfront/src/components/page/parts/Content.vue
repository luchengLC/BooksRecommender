<template>
  <div style="margin: 0; padding: 0;">
    <div class="mainContent" style="margin: 0; padding: 0">
      <div class="search-bar">
        <div class="div-input">
          <el-input class="search-input" placeholder="搜索..." v-model="searchInput"
                    @keyup.enter.native="searchHandle(1)"></el-input>
          <el-button class="search-btn" slot="append" icon="el-icon-search" @click="searchHandle(1)"
                     v-loading.fullscreen.lock="fullscreenLoading"></el-button>
        </div>
      </div>

      <!--页面初始化时的热门-->
      <h3 class="page-title" v-if="showInitHot"><i class="el-icon-menu"></i>热门</h3>
      <ul class="books-hot-init" v-if="showInitHot">
        <li class="book-item" v-for="(item, index) in hotBooks" :key="item.bookId">
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
      <h3 class="page-title" v-if="showSearchResult"><i class="el-icon-menu"></i>{{resultTitle}}</h3>
      <ul class="books-container" v-if="showSearchResult">
        <li class="book-item" v-for="(item, index) in books" :key="item.bookId">
          <div class="pic">
            <a target="_blank" :href="item.subjectUrl" :title="item.bookName">
              <img :src="item.imgUrl" :alt="item.bookName">
            </a>
          </div>
          <div class="info">
            <h2 class="bname">
              <a target="_blank" class="aname" :href="item.subjectUrl">{{item.bookName}}</a>
              <el-button class="collect" type="primary" plain size="medium" @click="handleCollect(item)">
                收藏
              </el-button>
              <!--<span>我的评分：<span style="color: #ff994b">4 stars</span>/5 stars</span>-->
            </h2>
            <p class="publi">{{item.author}} / {{item.publisher}} / {{item.pubDate}} / {{item.price}}</p>
            <div class="evaluate">
              <span>评分：</span>
              <span class="score">{{item.ratingScore}}</span>
              <span class="num">（{{item.ratingNum}}人评价）</span>
            </div>
            <p class="brief">{{item.summary}}</p>
            <div class="tags">
              <span class="span-tag"
                    v-for="(i, index2) in item.tags" :key="i.tags">
              {{i.tagName}}</span>
            </div>

          </div>

        </li>
      </ul>
      <!---->
      <!--分页，翻页器-->
      <div class="page" v-if="showSearchResult">
        <el-pagination
          @current-change="handleCurrentChange"
          background
          layout="prev, pager, next"
          :page-size="20"
          :total="itemCount">
        </el-pagination>
      </div>
    </div>

    <!--右侧-->
    <div class="hotContent" v-if="showSearchResult">
      <div style="margin: 50px 0 0 0; padding: 0">
        <!--标签推荐-->
        <h3 class="right-page-title">
          <span class="title">
            <i class="el-icon-menu"></i>
            标签推荐
          </span>
          <el-button type="text" class="refresh-btn" :loading="refreshTagBtnLoad" @click="handleRecommendTags">
            刷新
          </el-button>
        </h3>
        <!--<el-button type="text" style="margin: 0; padding: 0"></el-button>-->
        <div class="tags">
          <p style="color: rgb(84, 92, 100);" v-if="hadLogin===false"><i class="el-icon-warning"></i> 登录后才能为您推荐！</p>
          <el-button class="tag-btn" type="text" v-for="(i, index2) in tags"
                     :key="i.tags"
                     v-if="hadLogin===true" @click="tagSearch(i.tagName, 1)">
             <span class="span-tag">
              {{i.tagName}}</span>
          </el-button>
        </div>

        <!--书籍推荐-->
        <h3 class="right-page-title">
          <span class="title">
            <i class="el-icon-menu"></i>
            书籍推荐
          </span>
          <el-button type="text" class="refresh-btn">刷新</el-button>
        </h3>

        <ul class="books-recommend">
          <p style="color: rgb(84, 92, 100);" v-if="hadLogin===false"><i class="el-icon-warning"></i> 登录后才能为您推荐！</p>
          <li class="book-item" v-for="(item, index) in bookRec" :key="item.bookId" v-if="hadLogin===true">
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
              <el-button class="collect" type="primary" plain size="medium">
                收藏
              </el-button>
            </div>
          </li>
        </ul>


        <h3 class="right-page-title">
          <span class="title">
            <i class="el-icon-menu"></i>
            HOT
          </span>
        </h3>

        <ul class="books-hot">
          <li class="book-item" v-for="(item, index) in hotBooks" :key="item.bookId">
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
              <el-button class="collect" type="primary" plain size="medium">
                收藏
              </el-button>
            </div>
          </li>
        </ul>
      </div>
    </div>


    <!--收藏对话框-->
    <el-dialog
      title="收藏"
      :visible.sync="dialogCollectVisible"
      width="500px"
      :before-close="handleCollectCansel">
      <div v-if="hadCollect===false">
        <p>请给书籍 《{{collectItem.bookName}}》 评收藏分：</p>
        <div class="rate">
          <el-rate
            v-model="valueCollectStarSet"
            show-score
            text-color="#ff9900"
            score-template="{value}"
            show-text
            style="margin-top: 2px">
          </el-rate>
          <span>{{texts[valueCollectStarSet]}}</span>
        </div>

      </div>
      <div v-if="hadCollect===true">
        <p>您曾于<span class="cbName">{{collectTime}}</span></p>
        <p>收藏了书籍 <span class="cbName">《{{collectItem.bookName}}》</span>：</p>
        <div class="rate">
          <el-rate
            disabled
            v-model="valueCollectStarGet"
            show-score
            score-template="{value}"
            text-color="#ff9900"
            style="margin-top: 2px">
          </el-rate>
          <span>{{texts[valueCollectStarGet]}}</span>
        </div>

        <p>您不需要再次收藏！</p>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="handleCollectCansel">取 消</el-button>
        <el-button type="primary" @click="handleCollectSubmit">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import ElButton from '../../../../node_modules/element-ui/packages/button/src/button'
  import bus from '../../../assets/eventBus'
  export default {
    components: {ElButton},
    data () {
      return {
        baseUrl: 'http://127.0.0.1:8000/recommend/',
        userId: '13411977340',
        hadLogin: false,
        value4: "5",
        showSearchResult: false,
        fullscreenLoading: false,
        showInitHot: true,
        searchInput: '',
        itemCount: 0,  // 控制页数
        curPage: 0,
        dialogCollectVisible: false,  // 收藏 对话框是否可见
        hadCollect: false,  // 未评分 控制 显示
        valueCollectStarGet: 0,
        valueCollectStarSet: 0,
        refreshTagBtnLoad: false,
        refreshBookBtnLoad: false,
        resultTitle: '搜索结果',
        searchTag: '',
        collectItem: {
          bookName: '',
          bookId: '',
          starNum: '',
        },

        texts: ['', '极差', '较差', '还行', '推荐', '力荐'],
        books: [],
        tags: [],
        hotBooks: [
          {
            bname: '神迹',
            bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
            imgUrl: 'https://img1.doubanio.com/mpic/s29708619.jpg',
            author: '[爱尔兰] 爱玛·多诺霍'
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
        this.fullscreenLoading = false;
        this.refreshTagBtnLoad = false;
        this.refreshBookBtnLoad = false;
        this.resultTitle = '搜索结果';
        this.itemCount = 0;
        // hot books api

        this.getValueFromTopBar()  // 获取userId 从TopBar
        // 标签推荐、 书籍推荐接口
        this.handleRecommendTags()

//        this.handleRecommendBooks()
      })
    },
    watch: {
      '$route'(to, from){
        if (to.name === 'main' && from.name === 'favor') {
          let searchState = this.$route.params.searchState;
          if (searchState === 1) {
            this.showSearchResult = true;
            this.showInitHot = false;

            this.userId = this.$route.params.userId;
            this.searchInput = this.$route.params.searchInput;
            this.searchHandle(1);
          }
        }
      }
    },
    methods: {
      getValueFromTopBar() {
        let _this = this;
        bus.$on("getUserId", function (userId) {
          _this.userId = userId;
        });
        console.log('当前userId = ' + this.userId);
      },
      searchHandle(pageno){
        this.curPage = pageno;
        if (this.searchInput === '') {
          this.$message.error('请输入搜索内容！')
        } else {
          // 显示模块
          this.showSearchResult = true;
          this.showInitHot = false;
          this.resultTitle = '搜索结果';

          let wd = encodeURIComponent(this.searchInput);
          let url = this.baseUrl + 'book/search?wd=' + wd + '&pageno=' + pageno;

          this.fullscreenLoading = true;

          let _this = this;

          this.$axios.get(url)
            .then((response) => {
              let res = response.data;
              console.log('search response.data ====');
              console.log(res);
              if (res['error_code'] === 0) {
                _this.books = res['data']['list'];
                _this.$message.success(res['msg']);
                _this.itemCount = res['data']['page_count'] * 20
              } else {
                _this.$message.error(res['msg']);
              }
              _this.fullscreenLoading = false;
            })
            .catch(function (err) {
              console.log(err);
              console.log('searchHandle' + err)
              _this.$message.error('搜索异常！请重搜！')
              _this.fullscreenLoading = false;
            });
        }
      },
      handleCurrentChange(currentPage) {  // 翻页跳转
        if (this.resultTitle === '搜索结果') {
          this.searchHandle(currentPage);
        } else {
          this.handleTagSearch(currentPage);
        }

      },
      handleCollect(item) {
        if (this.userId === '' || this.userId === null) {
          this.$message.warning('请先注册/登录系统！')
        } else {
          console.log(this.userId);
          console.log(item.bookId);
          // 获取书本评价信息
          this.collectItem['bookId'] = item.bookId;
          this.collectItem['bookName'] = item.bookName;

          let url = this.baseUrl + 'star/query';

          let params = new URLSearchParams();
          params.append('userId', this.userId);
          params.append('bookId', item.bookId);

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
                if (res['data']['starState'] === 1) {  // 用户已评分
                  _this.hadCollect = true;
                  _this.valueCollectStarGet = res['data']['star']
                  _this.collectTime = _this.getLocalTime(res['data']['starTime']);

                } else {    // 用户未评分
                  _this.hadCollect = false;
                }
                _this.collectBookName = item.bookName;
                _this.dialogCollectVisible = true;
              } else {
                _this.$message.error(res['msg']);
              }
            })
            .catch(function (err) {
              console.log('star query error === ' + err);
              _this.$message.error('收藏详情操作异常！请重试！');
            });
        }
      },
      handleCollectCansel(done) {
        this.dialogCollectVisible = false;
        // 复原
        this.valueCollectStarSet = 0;
        this.collectItem.bookId = '';
        this.collectItem.bookName = '';
        this.collectItem.starNum = '';
      },
      handleCollectSubmit(done) {
        if (this.hadCollect === true) {
          this.dialogCollectVisible = false;
        } else {
          // 收藏 add api
          console.log(this.collectItem)

          // api
          let url = this.baseUrl + 'favor/add';
          let nowTimeStamp = Math.round(new Date().getTime() / 1000);  // 弄成秒级的 10位 的timestamp，数据库int类型 最大是11位
          let params = new URLSearchParams();
          params.append('userId', this.userId);
          params.append('bookId', this.collectItem.bookId);
          params.append('starNum', this.valueCollectStarSet);
          params.append('starTime', nowTimeStamp);

          console.log('params ===');
          console.log(params);

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
              console.log(res);
              if (res['error_code'] === 0) {
                _this.$message.success(res['msg']);
                _this.dialogCollectVisible = false;
              } else {
                _this.$message.error(res['msg']);
              }
            })
          // 复原
          this.valueCollectStarSet = 0;
          this.collectItem.bookId = '';
          this.collectItem.bookName = '';
          this.collectItem.starNum = '';
        }
      },
      // 得到当前时间的10位timestamp
      getLocalTime(tm) {
        return new Date(tm * 1000).toLocaleString().replace(/\//g, "-");
      },
      // 标签推荐
      handleRecommendTags(){
        if (this.userId === '') {
          this.hadLogin = false;
        } else {
          this.hadLogin = true;
          let url = this.baseUrl + 'rec/tags';

          let params = new URLSearchParams();
          params.append('userId', this.userId);

          this.refreshTagBtnLoad = true;

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
              if (res['error_code'] === 0) {
                console.log('标签 --------------- ')
                console.log(res['data']);
                _this.tags = res['data'];
              } else {
                _this.$message.error(res['msg']);
              }
              _this.refreshTagBtnLoad = false;
            })
            .catch(function (err) {
              console.log('tags rec error === ' + err);
              _this.$message.error('获取推荐标签操作异常！');
              _this.refreshTagBtnLoad = false;
            });
        }
      },
      // 书籍推荐
      handleRecommendBooks(){
        if (this.userId === '') {
          this.hadLogin = false;
        } else {
          this.hadLogin = true;
          let url = this.baseUrl + 'rec/books';

          let params = new URLSearchParams();
          params.append('userId', this.userId);

          this.refreshBookBtnLoad = true;

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
              if (res['error_code'] === 0) {
                _this.tags = res['data'];
              } else {
                _this.$message.error(res['msg']);
              }
              _this.refreshBookBtnLoad = false;
            })
            .catch(function (err) {
              console.log('tags rec error === ' + err);
              _this.$message.error('获取推荐书籍操作异常！');
              _this.refreshBookBtnLoad = false;
            });
        }
      },
      // 根据推荐标签 来搜索
      handleTagSearch(pageno){
        this.curPage = pageno;
        let wd = this.searchTag;
        this.resultTitle = '标签 “'+wd+ '” 搜索结果';
        console.log('wd ----', wd);
        let url = this.baseUrl + 'rec/tag/search?wd=' + wd + '&pageno=' + pageno;

        this.fullscreenLoading = true;

        let _this = this;

        this.$axios.get(url)
          .then((response) => {
            let res = response.data;
            console.log('tags search response.data ====');
            console.log(res);
            if (res['error_code'] === 0) {
              _this.books = res['data']['list'];
              _this.$message.success(res['msg']);
              _this.itemCount = res['data']['page_count'] * 20
            } else {
              _this.$message.error(res['msg']);
            }
            _this.fullscreenLoading = false;
          })
          .catch(function (err) {
            console.log(err);
            console.log('searchHandle' + err)
            _this.$message.error('搜索异常！请重搜！')
            _this.fullscreenLoading = false;
          });
      },
      tagSearch(wd, pageno) {
          console.log('get tag name'+wd);
          this.searchTag = wd;
          console.log('get tag name'+this.searchTag);
          this.handleTagSearch(pageno)
      }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .mainContent {
    display: -webkit-flex; /* Safari  chrome */
    display: flex;
    flex: 5;
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
      font-size: 20px;
      font-weight: bold;
      color: #F56C6C;
      text-align: left;
      padding-top: 5px;
      border-top: 1px solid #ddd;
      margin-top: 30px;
      .el-icon-menu {
        margin-right: 10px;
      }
    }

    .books-hot-init {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: row; /* 方向 横   左到右*/
      flex-wrap: wrap; /* 换行 */
      margin: 5px 5px 30px 5px;
      color: #666;
      width: 100%;
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
            min-width: 100px;
            min-height: 145px;
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
            .collect {
              padding: 1px 4px 1px 4px;
              margin-left: 30px;
              color: #ff994b;
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

            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
          }
          .tags {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
            flex-direction: row; /* 方向 横*/
            flex-wrap: wrap; /* 不换行 */
            span {
              margin: 1px 10px 1px 1px;
              padding: 1px 5px 1px 5px;
              background-color: #d1d1d1;
              color: #37A;
              font-size: 13px;
            }

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
    flex: 2;
    max-width: 500px;
    min-width: 130px;
    /*display: none;*/
    /*flex: 2;*/
    /*-webkit-box-shadow: #777 0 0 2px;*/
    /*-moz-box-shadow: #777 0 0 2px;*/
    /*box-shadow: #777 0 0 2px;*/

    margin: 20px 0 0 50px;
    .right-page-title {
      text-align: left;
      padding-bottom: 3px;
      margin-bottom: 16px;
      margin-left: 15px;
      border-bottom: 1px solid #ddd;
      .el-icon-menu {
        margin-right: 10px;
      }
      .title {
        font-size: 20px;
        font-weight: bold;
        color: #F56C6C;
      }
      .refresh-btn {
        float: right;
        font-size: 14px;
        &:hover {
          text-decoration: underline;
        }
      }
    }

    .tags {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: row; /* 方向 横*/
      flex-wrap: wrap; /* 换行 */
      margin-left: 10px;
      .tag-btn {
        padding-top: 0;
        margin: 1px 10px 5px 1px;
        span {
          padding: 1px 5px 1px 5px;
          background-color: #d1d1d1;
          color: #37A;
          font-size: 15px;
        }
      }

    }

    .books-hot, .books-recommend {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      flex-direction: row; /* 方向 横   左到右*/
      flex-wrap: wrap; /* 换行 */
      margin: 5px 5px 0 10px;
      color: #666;
      .book-item {
        text-align: left;
        margin-bottom: 10px;
        font-size: 12px;
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
          .collect {
            padding: 1px 4px 1px 4px;
            color: #ff994b;
            float: right;
          }
        }
      }
    }
  }

  .cbName {
    color: #F56C6C;;
  }

  .rate {
    display: -webkit-flex; /* Safari  chrome */
    display: flex;
    flex-direction: row; /* 方向 横*/
    flex-wrap: nowrap; /* 换行 */
    justify-content: center;

    span {
      margin-left: 10px;
      color: #ff9900;
    }
  }

</style>
