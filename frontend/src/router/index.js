import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import ImageSimilarity from '@/views/ImageSimilarity.vue'
import DataSimilarity from '@/views/DataSimilarity.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landingPage',
      component: LandingPage
    },
    {
      path: '/imageSimilarity',
      name: 'imageSimilarity',
      component: ImageSimilarity
    },
    {
      path: '/dataSimilarity',
      name: 'dataSimilarity',
      component: DataSimilarity
    }
  ]
})

export default router
