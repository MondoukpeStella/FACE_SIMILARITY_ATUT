<template>
  <NavBar :state="value"></NavBar>
  <div
    class="flex-col font-montserrat relative sm:flex sm:justify-center sm:items-center min-h-screen bg-center bg-gray-100 selection:bg-red-500 selection:text-white"
    style="background-image: url('/background.jpg'); background-size: cover"
  >
    <div class="max-w-7xl mx-auto p-2 lg:p-2">
      <div class="">
        <div class="mb-4">
          <h1 class="font-bold text-center text-3xl text-white">
            Plongez dans notre technologie de similarité faciale
          </h1>
          <div class="text-center text-white pt-4">
            <h1 id="typewriter" class="text-2xl text-center"></h1>
          </div>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8 lg:mt-4 w-full">
      <div
        class="w-full justify-start items-center scale-100 p-6 text-white from-gray-700/50 via-transparent rounded-lg shadow-2xl shadow-gray-500/20 flex motion-safe:hover:scale-[1.01] transition-all duration-250 focus:outline focus:outline-2 focus:outline-red-500"
      >
        <div class="w-1/2 ml-8">
          <h2 class="mt-6 text-xl font-semibold dark:text-white">Similarité faciale</h2>

          <p class="mt-4 text-lg leading-relaxed">
            Comparez vos photos avec celles de vos amis, célébrités ou inconnus. Simple, rapide et
            amusant !
          </p>
          <router-link to="/imageSimilarity">
            <button
              class="mt-2 inline-flex items-center px-4 py-4 bg-blue-600 border border-transparent font-semibold text-xs text-white uppercase tracking-widest hover:bg-gray-700 focus:bg-gray-700 active:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition ease-in-out duration-150"
            >
              Testez maintenant
            </button>
          </router-link>
        </div>
      </div>
      <div></div>
      <div></div>
      <div
        class="w-full justify-end items-center scale-100 p-6 text-white from-gray-700/50 via-transparent rounded-lg shadow-2xl shadow-gray-500/20 flex motion-safe:hover:scale-[1.01] transition-all duration-250 focus:outline focus:outline-2 focus:outline-red-500"
      >
        <div class="w-1/2">
          <h2 class="mt-6 text-xl font-semibold">Précison des résultats</h2>

          <p class="mt-4 text-lg leading-relaxed">
            Nos algorithmes utilisent l’IA pour fournir des comparaisons précises. Voyez à qui vous
            ressemblez vraiment
          </p>
          <router-link to="/imageSimilarity">
            <button
              class="mt-2 inline-flex items-center px-4 py-4 bg-blue-600 border border-transparent font-semibold text-xs text-white uppercase tracking-widest hover:bg-gray-700 focus:bg-gray-700 active:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition ease-in-out duration-150"
            >
              En savoir plus
            </button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import NavBar from '@/components/NavBar.vue'
import { onMounted, ref } from 'vue'

const words = [`Comparez vos photos en quelques clics. Découvrez la magie de l’IA`]
let i = 0
let j = 0
let currentWord = ''
let isDeleting = false
const value = ref('home')
onMounted(() => {
  type()
})
function type() {
  currentWord = words[i]
  if (isDeleting) {
    document.getElementById('typewriter').textContent = currentWord.substring(0, j - 1)
    j--
    if (j == 1) {
      isDeleting = false
      i++
      if (i == words.length) {
        i = 0
      }
    }
  } else {
    document.getElementById('typewriter').textContent = currentWord.substring(0, j + 1)
    j++
    if (j == currentWord.length) {
      isDeleting = true
    }
  }
  setTimeout(type, 100)
}
</script>
