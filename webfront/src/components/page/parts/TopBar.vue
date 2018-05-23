<template>
  <div style="margin: 0; padding: 0">
    <el-menu
      class="el-menu"
      mode="horizontal"
      background-color="#545c64"
      text-color="#ffffff"
      active-text-color="#409EFF">
      <el-button class="menu-btn" type="text" id="sysName" @click="loaderMain">书籍推荐系统</el-button>
      <el-button class="menu-btn" type="text" id="favor" @click="loaderFavor">{{ btnFavor }}</el-button>

      <el-button class="menu-btn" type="text" id="register" @click="dialogRegisterVisible=true" v-if="hadLogin===false">
        {{ btnRegister }}
      </el-button>
      <el-button class="menu-btn" type="text" id="login" @click="dialogLoginVisible=true" v-if="hadLogin===false">
        {{ btnLogin }}
      </el-button>

      <el-button class="menu-btn" type="text" id="logout" @click="dialogLogoutVisible=true" v-if="hadLogin===true">
        {{ btnLogout }}
      </el-button>
      <el-button class="menu-btn" type="text" id="name">{{ btnName }}</el-button>
    </el-menu>


    <!--登录 对话框-->
    <el-dialog
      title="登录"
      :visible.sync="dialogLoginVisible"
      width="500px"
      :before-close="handleLoginCansel">
      <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="90px">
        <el-form-item label="账号" prop="userId">
          <el-input type="text" v-model="loginForm.userId" placeholder="6-18位数字字母组合..."></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" placeholder="密码..."></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleLoginCansel">取 消</el-button>
        <el-button type="primary" @click="handleLoginSubmit">确 定</el-button>
      </span>
    </el-dialog>

    <!--注册 对话框-->
    <el-dialog
      title="注册"
      :visible.sync="dialogRegisterVisible"
      width="500px"
      :before-close="handleRegisterCansel">
      <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="90px">
        <el-form-item label="账号" prop="userId">
          <el-input v-model="loginForm.userId" placeholder="18位数字字母组合..."></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="nickname">
          <el-input v-model="loginForm.nickname" placeholder="昵称..."></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" placeholder="密码..."></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="loginForm.email" placeholder="邮箱..."></el-input>
        </el-form-item>

      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleRegisterCansel">取 消</el-button>
        <el-button type="primary" @click="handleRegisterSubmit">确 定</el-button>
      </span>
    </el-dialog>

    <!--退出 对话框-->
    <el-dialog
      title="退出"
      :visible.sync="dialogLogoutVisible"
      width="500px"
      :before-close="handleLogoutCansel">
      <p>您是否确定退出登录？</p>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleLogoutCansel">取 消</el-button>
        <el-button type="primary" @click="handleLogoutSubmit">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
  import bus from '../../../assets/eventBus'
  import md5 from 'js-md5';

  export default {
    name: 'HelloWorld',
    data () {
      return {
        baseUrl: 'http://127.0.0.1:8000/recommend/',
        fullscreenLoading: false,
        userId: '',
        userIdTmp: '',
        nickname: '',
        dialogLoginVisible: false,
        dialogRegisterVisible: false,
        dialogLogoutVisible: false,
        btnFavor: '我喜爱列表',
        btnRegister: '注册',
        btnLogin: '登录',
        btnName: '',
        btnLogout: '退出',
        activeIndex: '',
        hadLogin: false,  // 默认登录状态是未登录
        loginForm: {
          userId: '',
          password: '',
          nickname: '',
          email: '',
        },
        registerForm: {},
        rules: {
          userId: [
            {required: true, message: '请输入账号', trigger: 'blur'},
//          {pattern: /^[a-zA-Z](\w){5,17}$/, message: '以字母开头，长度在6-18之间， 只能包含字符、数字和下划线', trigger: 'blur'}
            {pattern: /^(\w){6,18}$/, message: '6-18个字母、数字、下划线组合', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'},
            {min: 6, max: 30, message: '长度在 6 到 30 个字符', trigger: 'blur'},
            {pattern: /^(\w){6,20}$/, message: '只能输入6-20个字母、数字、下划线', trigger: 'blur'}
          ],
          nickname: [
            {required: true, message: '请输入昵称', trigger: 'blur'},
          ],
          email: [
//            {required: true, message: '请输入邮箱', trigger: 'blur'},
            {
              pattern: /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/,
              message: '请输入正确的邮箱地址',
              trigger: 'blur'
            }
          ]
        },

      }
    },
    mounted: function () {
      this.btnName = '游客';
      this.nickname = '游客';
      this.checkLogin();
      this.$nextTick(function () {
        this.fullscreenLoading = false;
        this.hadLogin = false;
      })
    },
    methods: {
      loaderFavor() {
          if (this.userId === '' || this.userId == null){
              this.$message.error('请先注册/登录系统！')
          } else {
            this.$router.push({name: 'favor', params: {userId: this.userId}});
          }
//      if (this.userId === '' || this.nickname === '游客' || this.nickname === '') {
//        this.$message.error('您还未注册或登录！请先进行注册登录操作！')
//      } else {
//        // console.log('转跳到 通知列表')
//        // console.log('现在username  = '+this.username)
//        this.$router.push({name: 'favor', params: {userId: userId}});
//      }
      },
      loaderMain(){
        this.$router.push({name: 'main'});
      },
      handleLoginCansel(done) {  //登录
        this.dialogLoginVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
      },
      handleRegisterCansel(done) {  // 注册
        //
        this.dialogRegisterVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
      },
      handleLogoutCansel(done) {  // 退出
        //
        this.dialogLogoutVisible = false;
      },

      //dialogLogoutVisible
      handleLoginSubmit(){  //登录
        let _this = this;
        // 处理
        this.$refs['loginForm'].validate((valid) => {
          if (valid) {

            let url = this.baseUrl + 'user/login'
            let params = new URLSearchParams();
            params.append('userId', this.loginForm.userId);       //你要传给后台的参数值 key/value
            params.append('password', md5(this.loginForm.password));
            let nowTimeStamp = Math.round(new Date().getTime() / 1000);  // 弄成秒级的 10位 的timestamp，数据库int类型 最大是11位
            params.append('startTime', nowTimeStamp);
            console.log('nowTimeStamp' + nowTimeStamp)
            this.userIdTmp = this.loginForm.userId;

            _this = this;

            this.$axios({
              method: 'post',
              url: url,
              data: params
            })
              .then(function (response) {
                if (response.data.error_code == 0) {

                  let res = response.data;
                  console.log(res)
                  _this.hadLogin = true;
                  _this.btnName = res['data']['nickname'];
                  _this.nickname = _this.btnName;  // nickname 是昵称的缓存
                  _this.userId = _this.userIdTmp;

                  // 先清除掉原来的token
                  _this.delCookie('token');

                  // token 存储在 cookie
                  let endTime = res['data']['endTime'];
                  let token = res['data']['token'];
                  // setCookie()
                  _this.setCookie('token', token, endTime);

                  _this.sendValueToContents();  // 给TopBar传值
                } else {
                  _this.hadLogin = false;
                  _this.btnName = '游客';
                  _this.nickname = '游客';
                }
                _this.$message.success(response.data.msg);
              })
              .catch(function (error) {
                console.log(error)
              });
            this.dialogLoginVisible = false;
            this.$refs['loginForm'].resetFields();  // 清空
          } else {
            _this.$message.error('登录不成功！');
            return false;
          }
        });
      },
      handleRegisterSubmit(){  // 注册
        let _this = this;
        // 处理
        this.$refs['loginForm'].validate((valid) => {
          if (valid) {
            let url = this.baseUrl + 'user/register'
            let params = new URLSearchParams();
            params.append('userId', this.loginForm.userId);       //你要传给后台的参数值 key/value
            params.append('password', this.loginForm.password);
            params.append('nickname', this.loginForm.nickname);
            params.append('email', this.loginForm.email);
            let nowTimeStamp = Math.round(new Date().getTime() / 1000);  // 弄成秒级的 10位 的timestamp，数据库int类型 最大是11位
            params.append('startTime', nowTimeStamp);

            this.userIdTmp = this.loginForm.userId;

            this.$axios({
              method: 'post',
              url: url,
              data: params
            })
              .then(function (response) {
                  let res = response.data;
                  console.log('register ------- ');
                  console.log(res)
                if (res['error_code'] === 0) {
                  _this.hadLogin = true;
                  _this.btnName = res['data']['nickName'];
                  _this.nickName = res['data']['nickName'];
                  _this.userId = res['data']['userId'];

                  // token 存储在 cookie
                  let endTime = res['data']['endTime'];
                  let token = res['data']['token'];
                  // setCookie()
                  _this.setCookie('token', token, endTime);

                  _this.sendValueToContents();  // 给TopBar传值
                } else {
                  _this.hadLogin = false;
                }
              })
              .catch(function (error) {
                _this.$message.error('注册异常！');
              });
            this.dialogRegisterVisible = false;
            this.$refs['loginForm'].resetFields();  // 清空
          } else {
            _this.$message.error('注册不成功！');
            return false;
          }
        });
      },
      handleLogoutSubmit(){  // 退出
        let _this = this;
        let url = this.baseUrl + 'user/logout';
        this.userIdTmp = this.loginForm.userId;
        let token = this.getCookie('token');
        let params = new URLSearchParams();
        params.append('token', token);
        this.$axios({
          method: 'post',
          url: url,
          data: params,
        })
          .then((response) => {
            let res = response.data;
            console.log(res);
            if (res.error_code === 0) {
              _this.btnName = res['data']['nickName'];
              _this.userId = res['data']['userId'];
              _this.sendValueToContents();  // 给TopBar传值

              // 删除 cookie 中 token
              _this.delCookie('token')

              _this.hadLogin = false;

              _this.dialogLogoutVisible = false;
              _this.fullscreenLoading = false;

              // 跳回首页
              _this.getIndex();
              // 重新刷新——更新Cookie变化
//              location.reload()
            } else {
              // console.log(res['msg']);
              _this.fullscreenLoading = false;
            }
          })
      },
      // 维护登录状态 1526198547  1526284947   endtime=1526297165  startTime = 1526210834
      checkLogin() {
        let params = new URLSearchParams();

        let token = this.getCookie('token');
        let nowTimeStamp = Math.round(new Date().getTime() / 1000);  // 弄成秒级的 10位 的timestamp，数据库int类型 最大是11位
        params.append('startTime', nowTimeStamp);
        params.append('token', token);

        console.log(token)
        console.log(nowTimeStamp)

        let url = this.baseUrl + 'user/home';
        let _this = this;
        this.$axios({
          method: 'post',
          url: url,
          data: params,
        })
          .then((response) => {
            let res = response.data;
            console.log(res);
            if (res['error_code'] === 0) {
              if (res['data']['state_code'] === 0) {
                _this.btnName = res['data']['nickName'];
                _this.nickname = res['data']['nickName'];
                _this.userId = res['data']['userId'];
                _this.sendValueToContents();  // 给TopBar传值
                _this.hadLogin = true;

              } else {
                _this.hadLogin = false;
                _this.$message.warning(res['data']['msg'])
              }
            } else {
              // console.log(res['msg']);
            }
          })
      },
      getFocus(username) {
        // console.log(this.username)
        // console.log(this.name)
        if (this.username === '' || this.name === '游客' || this.name === '') {
          this.$message.error('您还未注册或登录！请先进行注册登录操作！')
        } else {
          // console.log('转跳到 通知列表')
          // console.log('现在username  = '+this.username)
          this.$router.push({name: 'focus', params: {username: username}});
        }
      },
      getIndex() {
        this.fullscreenLoading = false;
        this.$router.push({name: 'main'});
      },
      sendValueToContents() {
        let _this = this;
        bus.$emit("getUserId", _this.userId);
        console.log('来到sendValueToContents，userid = '+ this.userId)
      },

      // 换回时间字符串
      getLocalTime(tm) {
        return new Date(tm * 1000).toLocaleString().replace(/\//g, "-");
      },
      // 获取cookie中token
      getCookie(cname) {
        let name = cname + "=";
        let ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
          let c = ca[i];
          while (c.charAt(0) === ' ') c = c.substring(1);
          if (c.indexOf(name) !== -1) return c.substring(name.length, c.length);
        }
        return "";
      },
      //设置cookie   name为cookie的名字，value是值，tm为过期时间10位时间戳
      setCookie (name, value, tm) {
        let exdate = new Date();
        exdate.setTime(tm * 1000);
        document.cookie = name + "=" + escape(value) + ((tm === null) ? "" : ";expires=" + exdate.toGMTString());
      },
      //删除cookie
      delCookie (name) {
        let exp = new Date();
        exp.setTime(exp.getTime() - 1);
        let cval = this.getCookie(name);
        console.log('删除cookie ing -------')
        if (cval !== null)
          document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
      }

    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .el-menu {
    text-align: left;
    .menu-btn {
      height: 50px;
      line-height: 0;
      margin: 0 20px 0 5px;
      /*color: #ffd04b;*/
      font-size: 20px;

      &:hover {
        /*color: #409EFF;;*/
      }
    }

    #sysName {
      color: #fff;
      &:hover {
        color: #409EFF;;
      }
    }

    #login, #register, #name, #logout {
      float: right;
    }
  }

  .el-dialog-div {
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>
