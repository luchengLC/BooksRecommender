<template>
  <div style="margin: 50px 0 0 0; padding: 0">
    <h2 class="hot" style="color:#F56C6C">热门推荐 TOP10</h2>
    <ul class="books-container">
      <li class="book-item" v-for="(item, index) in books" :key="index">
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
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      books: [
        {
          bname: '蟹之进行曲1',
          bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
          imgUrl: 'https://img3.doubanio.com/lpic/s29517015.jpg',
          author: '[法] 阿尔蒂尔·德·潘'
        },
        {
          bname: '神迹',
          bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
          imgUrl: 'https://img1.doubanio.com/lpic/s29708619.jpg',
          author: '[爱尔兰] 爱玛·多诺霍'
        },
        {
          bname: '啊！这样就能辞职了',
          bookLink: 'https://book.douban.com/subject/27201290/?icn=index-editionrecommend',
          imgUrl: 'https://img3.doubanio.com/lpic/s29669694.jpg',
          author: '[日] 安倍夜郎'
        },
        {
          bname: '植物花卉插画图案集',
          bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
          imgUrl: 'https://img3.doubanio.com/lpic/s29708071.jpg',
          author: '[英] 鲍伊风尚'
        },
        {
          bname: '啊！这样就能辞职了',
          bookLink: 'https://book.douban.com/subject/27201290/?icn=index-editionrecommend',
          imgUrl: 'https://img3.doubanio.com/lpic/s29669694.jpg',
          author: '[日] 安倍夜郎'
        },
        {
          bname: '蟹之进行曲1',
          bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
          imgUrl: 'https://img3.doubanio.com/lpic/s29517015.jpg',
          author: '[法] 阿尔蒂尔·德·潘'
        },
        {
          bname: '神迹',
          bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
          imgUrl: 'https://img1.doubanio.com/lpic/s29708619.jpg',
          author: '[爱尔兰] 爱玛·多诺霍'
        },
        {
          bname: '植物花卉插画图案集',
          bookLink: 'https://book.douban.com/subject/30162092/?icn=index-editionrecommend',
          imgUrl: 'https://img3.doubanio.com/lpic/s29708071.jpg',
          author: '[英] 鲍伊风尚'
        },
        {
          bname: '蟹之进行曲1',
          bookLink: 'https://book.douban.com/subject/27113959/?icn=index-latestbook-subject',
          imgUrl: 'https://img3.doubanio.com/lpic/s29517015.jpg',
          author: '[法] 阿尔蒂尔·德·潘'
        },
        {
          bname: '神迹',
          bookLink: 'https://book.douban.com/subject/27600501/?icn=index-editionrecommend',
          imgUrl: 'https://img1.doubanio.com/lpic/s29708619.jpg',
          author: '[爱尔兰] 爱玛·多诺霍'
        }

      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .hot {
    font-weight: bold;
    padding-bottom: 3px;
    margin-bottom: 16px;
    border-bottom: 1px solid #ddd;
  }
  .books-container {
    display: -webkit-flex; /* Safari  chrome */
    display: flex;
    flex-direction: row; /* 方向 横   左到右*/
    flex-wrap: wrap; /* 换行 */
    margin: 5px 5px 0 5px;
    font-size: 12px;
    color: #666;
    .book-item {
      text-align: left;
      .pic {
        .a {
          color: #3377aa;
          font-size: 14px;
          text-decoration:none;
          .img {
            width: 115px;
            height: 172px;
          }
        }
      }
      .info {
        .title {
          width: 120px;
          white-space:nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          .a {
            color: #3377aa;
            font-size: 14px;
            text-decoration:none;
          }
        }
        .author {
          width: 120px;
          white-space:nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }
      }
    }
  }
</style>
