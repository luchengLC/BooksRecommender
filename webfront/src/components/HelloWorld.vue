<template>
  <div style="margin: 0; padding: 0">
    <el-menu
      :default-active="activeIndex2"
      class="el-menu"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b" >
      <el-menu-item class="el-menu-item" index="1">书籍推荐系统</el-menu-item>
      <el-menu-item class="el-menu-item" index="2">主页</el-menu-item>
      <el-menu-item class="el-menu-item" index="3">HOT</el-menu-item>
      <el-menu-item class="el-menu-item" index="4">我喜爱列表</el-menu-item>
      <el-menu-item class="el-menu-item" id="name-login" index="5">登录</el-menu-item>
      <el-menu-item class="el-menu-item" id="logout" index="6">注销</el-menu-item>
    </el-menu>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

  .el-menu, .el-menu > .el-menu-item {
    height: 30px;
    line-height: 30px;
  }

  #name-login, #logout {
    float: right;
  }

  #logout {
    /*display: none;*/
  }
</style>
