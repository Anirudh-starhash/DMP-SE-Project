import { createRouter, createWebHistory } from 'vue-router'
import index_page from '../components/other_module/IndexPage.vue'
import login_page from '../components/user_module/login_page.vue'
import register_page from '../components/user_module/register_page.vue'
import admin_page from '../components/admin_module/admin_page.vue'
import logout_page from '../components/admin_module/admin_logout.vue'
import user_logout_page from '../components/user_module/user_logout.vue'
import admin_dashboard from '../components/dashboard_module/admin_dashboard.vue'
import user_dashboard from '../components/dashboard_module/user_dashboard.vue'
import read_blogs from '@/components/blog_module/read_blogs.vue'
import create_blogs from '@/components/blog_module/create_blogs.vue'
import edit_blogs from '@/components/blog_module/edit_blogs.vue'
import read_admin_blogs from '@/components/blog_module/read_admin_blogs.vue'
import delete_blogs from '@/components/blog_module/delete_blogs.vue'
import admin_create_blogs from '@/components/blog_module/create_admin_blogs.vue'
import edit_admin_blogs from '@/components/blog_module/edit_admin_blogs.vue'
import delete_admin_blogs from '@/components/blog_module/delete_admin_blogs.vue'
import admin_edit_blogs from '@/components/blog_module/admin_edit_blog.vue'
import admin_delete_blogs from '@/components/blog_module/admin_delete_blogs.vue'
import other_users_page from '../components/user_module/other_users_page.vue'
import request_page from '@/components/other_module/request_page.vue'
import user_request_page from '@/components/other_module/user_request_page.vue'
import user_stats_page from '@/components/stats_module/user_stats_page.vue'
import user_status_page from '@/components/user_module/user_status_page.vue'
import admin_stats_page from '@/components/stats_module/admin_stats_page.vue'
import send_alert_form from '@/components/alert_module/send_alert_form.vue'
import create_admin_review from '@/components/reviews_module/create_admin_review.vue'
import create_review from '@/components/reviews_module/create_review.vue'
import delete_review from '@/components/reviews_module/delete_review.vue'
import delete_admin_review from '@/components/reviews_module/delete_admin_review.vue'
import edit_admin_review from '@/components/reviews_module/edit_admin_review.vue'
import edit_review from '@/components/reviews_module/edit_review.vue'
import read_admin_review from '@/components/reviews_module/read_admin_review.vue'
import read_review from '@/components/reviews_module/read_review.vue'
import change_password from '@/components/other_module/change_password.vue'
import monitor_page from '@/components/other_module/monitor_page.vue'
import forgot_password from '@/components/other_module/forgot_password.vue'
import PieChart from '@/components/stats_module/PieChart.vue'
import BarChart from '@/components/stats_module/BarChart.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index-page',
      component: index_page
    },
    {
      path:'/login_page',
      name:'login_page',
      component:login_page
    },

    {
      path:'/register_page',
      name:'register',
      component:register_page
    },
    {
      path: '/logout_page',
      name: 'logout_page',
      component: logout_page,
    },
    {
      path: '/user_logout_page/:id',
      name: 'user_logout_page',
      component: user_logout_page,
    },
    {
      path:'/admin_page',
      name:'admin_page',
      component:admin_page
    },
    {
      path: '/admin_dashboard',
      name: 'admin_dashboard',
      component: admin_dashboard,
    },

    {
      path: '/user_dashboard/:id',
      name: 'user_dashboard',
      component: user_dashboard,
    },
    {
      path: '/other_users_page/:id',
      name: 'other_users_page',
      component: other_users_page,
    },
    {
      path:'/blogs/:id',
      name:'read_blogs',
      component:read_blogs
    },
    {
      path:'/admin_blogs/:id',
      name:'read_admin_blogs',
      component:read_admin_blogs
    },
    {
      path:'/edit_blog/:id',
      name:'edit_blogs',
      component:edit_blogs
    },
    {
      path:'/create_blog/:id',
      name:'create_blogs',
      component:create_blogs
    },
    {
      path:'/delete_blog/:id',
      name:'delete_blogs',
      component:delete_blogs
    },
    {
      path:'/edit_admin_blogs/:id',
      name:'edit_admin_blogs',
      component:edit_admin_blogs
    },
    {
      path:'/create_admin_blog/:id',
      name:'create_admin_blogs',
      component:admin_create_blogs
    },
    {
      path:'/delete_admin_blogs/:id',
      name:'delete_admin_blogs',
      component:delete_admin_blogs
    },
    {
      path:'/admin_edit_blog/:id',
      name:'admin_edit_blogs',
      component:admin_edit_blogs
    },
    {
      path:'/admin_delete_blog/:id',
      name:'admin_delete_blogs',
      component:admin_delete_blogs
    },
    {
      path:'/request_page',
      name:'request_page',
      component:request_page
    },
    {
      path:'/user_request_page',
      name:'user_request_page',
      component:user_request_page
    },
    {
      path:'/user_stats_page/:id',
      name:'user_stats_page',
      component:user_stats_page
    },
    {
      path:'/user_status_page/:id',
      name:'user_status_page',
      component:user_status_page
    },
    {
      path:'/admin_stats_page',
      name:'admin_stats_page',
      component:admin_stats_page
    },
    {
      path:'/send_alert_form/:id',
      name:'send_alert_form',
      component:send_alert_form
    },
    {
      path:'/create_review/:id',
      name:'create_review',
      component:create_review
    },
    {
      path:'/create_admin_review/:id',
      name:'create_admin_review',
      component:create_admin_review
    },
    {
      path:'/edit_review/:id',
      name:'edit_review',
      component:edit_review
    },
    {
      path:'/edit_admin_review/:id',
      name:'edit_admin_review',
      component:edit_admin_review
    },
    {
      path:'/delete_review/:id',
      name:'delete_review',
      component:delete_review
    },
    {
      path:'/delete_admin_review/:id',
      name:'delete_admin_review',
      component:delete_admin_review
    },
    {
      path:'/read_review/:id',
      name:'read_review',
      component:read_review
    },
    {
      path:'/read_admin_review/:id',
      name:'read_admin_review',
      component:read_admin_review
    },
    {
      path:'/change_password',
      name:'change_password',
      component:change_password
    },
    {
      path:'/forgot_password',
      name:'forgot_password',
      component:forgot_password
    },
    {
      path:'/monitor_page',
      name:'monitor_page',
      component:monitor_page
    },
  ],

})

export default router
