
import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/page/MainPage'
import Favor from '@/components/page/MainPageFavor'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      meta: {
        keepAlive: true,
      },
      name: 'main',
      component: Main,

    },
    {
      path: '/favor',
      meta: {
        keepAlive: true,
      },
      name: 'favor',
      component: Favor,

    },
  ]
})

