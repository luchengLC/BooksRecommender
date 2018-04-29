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
      <el-menu-item class="el-menu-item" index="1">图书推荐系统</el-menu-item>
      <!--<el-menu-item class="el-menu-item" index="2">主页</el-menu-item>-->
      <!--<el-menu-item class="el-menu-item" index="3">HOT</el-menu-item>-->
      <el-menu-item class="el-menu-item" index="4">我喜爱列表</el-menu-item>
      <el-menu-item class="el-menu-item" id="name-login" index="5">登录</el-menu-item>
      <el-menu-item class="el-menu-item" id="logout" index="6">注销</el-menu-item>
    </el-menu>
  </div>
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
</style>
