// import Vue from 'vue'
// import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
//
// Vue.use(Router)
//
// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })

import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/pages/MainPage'
import Favor from '@/components/pages/MainPageFavor'
import New from '@/components/page/MainPage'
import NewFavor from '@/components/page/MainPageFavor'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/index',
      name: 'Main',
      component: Main
    },
    {
      path: '/favor',
      name: 'Favor',
      component: Favor
    },
    {
      path: '/',
      name: 'New',
      component: New
    },
    {
      path: '/fa',
      name: 'NewFavor',
      component: NewFavor
    },
  ]
})

