
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
      name: 'Main',
      component: Main
    },
    {
      path: '/favor',
      name: 'Favor',
      component: Favor
    },
  ]
})

