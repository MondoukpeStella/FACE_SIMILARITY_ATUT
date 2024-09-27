<template>
  <nav
    class="font-montserrat bg-white fixed w-full z-20 border-b border-gray-200"
  >
    <div class="flex items-center justify-between p-4">
      <div class="flex items-center space-x-3 pl-10">
        <img class="object-cover w-full h-full" src="../assets/logo_resize.png" alt="" />
      </div>
      <div
        class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1"
        id="navbar-sticky"
      >
        <ul
          class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white"
        >
          <router-link to="/">
            <li>
              <a
                href="#"
                class="block py-2 px-3 rounded md:bg-transparent md:p-0"
                :class="state == 'home' ? 'text-blue-700' : ''"
                aria-current="page"
                >HOME</a
              >
            </li>
          </router-link>
          <router-link to="/imageSimilarity">
            <li>
              <a
                href="#"
                class="block py-2 px-3 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover: md:p-0"
                :class="state == 'image' ? 'text-blue-700' : ''"
                >COMPARER DEUX IMAGES</a
              >
            </li>
          </router-link>
          <router-link to="/dataSimilarity">
            <li>
              <a
                href="#"
                class="block py-2 px-3 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0"
                :class="state == 'data' ? 'text-blue-700' : ''"
              >
                SYNCHRONISATION DES INFORMATIONS</a
              >
            </li>
          </router-link>
        </ul>
      </div>
      <div class="items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
        <button
          type="button"
          class="text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center"
        >
          <svg
            width="36px"
            height="36px"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <path
                d="M4 6H20M4 12H20M4 18H20"
                stroke="#000000"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              ></path>
            </g>
          </svg>
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
defineProps({
  state: {
    type: String,
    required: true
  }
})
</script>
