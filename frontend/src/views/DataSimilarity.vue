<template>
    <NavBar :state="value"></NavBar>
    <div v-if="similarity == null && loading == false"
        class="flex-col font-montserrat relative sm:flex sm:justify-center sm:items-center pt-36 bg-dots-darker bg-center selection:bg-red-500 selection:text-white">
        <img src="../assets/wiiru_logo.png" width="300px" height="300px" alt="">

        <div class="mx-auto p-2 lg:p-2 text-black">
            <div class="flex flex-col items-center justify-center">
                <div class="mb-4">
                    <h1 class="font-bold text-center text-3xl">SYNCHRONISEZ VOS DONNÉES</h1>
                    <p class="text-center text-sm">
                        Synchronisez deux bases de données à l'aide d'une simple photo
                    </p>
                </div>

                <div class="flex items-center justify-center w-full">
                    <label for="dropzone-file"
                        class="flex flex-col items-center justify-center py-9 w-full border border-gray-300 border-dashed rounded-2xl cursor-pointer bg-gray-50">
                        <div class="mb-3 flex items-center justify-center">
                            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"
                                fill="none">
                                <g id="Upload 02">
                                    <path id="icon"
                                        d="M16.296 25.3935L19.9997 21.6667L23.7034 25.3935M19.9997 35V21.759M10.7404 27.3611H9.855C6.253 27.3611 3.33301 24.4411 3.33301 20.8391C3.33301 17.2371 6.253 14.3171 9.855 14.3171V14.3171C10.344 14.3171 10.736 13.9195 10.7816 13.4326C11.2243 8.70174 15.1824 5 19.9997 5C25.1134 5 29.2589 9.1714 29.2589 14.3171H30.1444C33.7463 14.3171 36.6663 17.2371 36.6663 20.8391C36.6663 24.4411 33.7463 27.3611 30.1444 27.3611H29.2589"
                                        stroke="#4F46E5" stroke-width="1.6" stroke-linecap="round" />
                                </g>
                            </svg>
                        </div>
                        <h2 class="text-center text-gray-400 text-xs font-normal leading-4 mb-1">
                            PNG, JPG or PDF, smaller than 15MB
                        </h2>
                        <h4 class="text-center text-gray-900 text-sm font-medium leading-snug">
                            Upload your file here
                        </h4>
                        <input @change="(event) => handelFileUpload(event)" type="file" accept="image/*" name="image"
                            id="dropzone-file" multiple class="hidden" />
                    </label>
                </div>
            </div>
            <div class="flex items-center justify-center w-full">
                <div class="images flex items-center gap-4">
                    <div v-for="(src, index) in imageSrc" :key="index" class="images-lists">
                        <div class="w-24 h-24 pt-4">
                            <img :src="src" id="output" class="image-style object-cover w-full h-full" />

                            <div class="h-24 w-24" v-if="imageSrc">
                                <svg fill="#000000" height="16px" width="16px" version="1.1" id="Layer_1" class="mt-2"
                                    @click="removeItem(index)" xmlns="http://www.w3.org/2000/svg"
                                    xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 492 492"
                                    xml:space="preserve">
                                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                                    <g id="SVGRepo_iconCarrier">
                                        <g>
                                            <g>
                                                <path
                                                    d="M300.188,246L484.14,62.04c5.06-5.064,7.852-11.82,7.86-19.024c0-7.208-2.792-13.972-7.86-19.028L468.02,7.872 c-5.068-5.076-11.824-7.856-19.036-7.856c-7.2,0-13.956,2.78-19.024,7.856L246.008,191.82L62.048,7.872 c-5.06-5.076-11.82-7.856-19.028-7.856c-7.2,0-13.96,2.78-19.02,7.856L7.872,23.988c-10.496,10.496-10.496,27.568,0,38.052 L191.828,246L7.872,429.952c-5.064,5.072-7.852,11.828-7.852,19.032c0,7.204,2.788,13.96,7.852,19.028l16.124,16.116 c5.06,5.072,11.824,7.856,19.02,7.856c7.208,0,13.968-2.784,19.028-7.856l183.96-183.952l183.952,183.952 c5.068,5.072,11.824,7.856,19.024,7.856h0.008c7.204,0,13.96-2.784,19.028-7.856l16.12-16.116 c5.06-5.064,7.852-11.824,7.852-19.028c0-7.204-2.792-13.96-7.852-19.028L300.188,246z">
                                                </path>
                                            </g>
                                        </g>
                                    </g>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex items-center justify-center mt-4">
                <button class="mt-4 p-2 bg-blue-600 text-white" type="submit" @click.prevent="predict">
                    Synchronisez
                </button>
            </div>
            <div class="flex items-center justify-center pt-8" v-if="errors != null">
                <span class="text-red-700">{{ errors }}</span>
            </div>
        </div>
    </div>

    <LoaderCmp v-else-if="loading == true && similarity == null"></LoaderCmp>

    <div v-else class="pt-24 font-montserrat">
        <div>
            <div class="flex items-center justify-center pb-4">
                <span class="mt-4 text-center">Résultats de la recherche</span>
            </div>
            <div class="relative overflow-x-auto">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                        <tr>
                            <th scope="col" class="px-6 py-3">Image</th>
                            <th scope="col" class="px-6 py-3">First Name</th>
                            <th scope="col" class="px-6 py-3">Last Name</th>
                            <th scope="col" class="px-6 py-3">Adress</th>
                            <th scope="col" class="px-6 py-3">Age</th>
                            <th scope="col" class="px-6 py-3">Occupation</th>
                            <th scope="col" class="px-6 py-3">Nationality</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="bg-white border-b">
                            <th scope="row" class="px-6 py-4">
                                <img class="object-cover w-24 h-24" :src="imageSrc[0]" alt="Product" />
                            </th>
                            <td class="px-6 py-4">
                                {{ similarity.Lastname[0] }}
                            </td>
                            <td class="px-6 py-4">
                                {{ similarity.Firstname[0] }}
                            </td>
                            <td class="px-6 py-4">
                                {{ similarity.Adress[0] }}
                            </td>
                            <td class="px-6 py-4">
                                {{ similarity.Age[0] }}
                            </td>
                            <td class="px-6 py-4">
                                {{ similarity.Occupation[0] }}
                            </td>
                            <td class="px-6 py-4">
                                {{ similarity.Nationality[0] }}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div class="flex items-center justify-center w-full text-white p-4 gap-8">
                    <Button class="p-2 bg-blue-700" @click="load(similarity)">Télécharger le résultat </Button>
                    <button class="p-2 bg-blue-700" @click="clear()">Faire une autre recherche</button>
                </div>
            </div>
        </div>

    </div>
</template>
<script setup>
import NavBar from '@/components/NavBar.vue'
import LoaderCmp from '@/components/LoaderCmp.vue';
import axios from 'axios'
import { ref, onMounted } from 'vue'

const BASE_URL = import.meta.env.VITE_API_URL

const form = ref({
    media: {}
})

const imageSrc = ref([])

const selectedFiles = ref([])

const similarity = ref()

const value = ref('')

const errors = ref()

const loading = ref(false)

onMounted(() => {
    value.value = 'data'
})

const handelFileUpload = async (e) => {
    var files = e.target.files || e.dataTransfer.files
    if (!files.length) return

    for (let i = 0; i < files.length; i++) {
        selectedFiles.value.push(files[i])
        const src = URL.createObjectURL(files[i])
        imageSrc.value.push(src)
    }

    form.value.media = e.target.files[0]
}

const removeItem = (index) => {
    imageSrc.value.splice(index, 1)
}

function predict() {
    loading.value = true
    errors.value = ''
    const formData = new FormData()
    const imageInput = document.getElementById('dropzone-file')
    console.log(loading.value);


    if (imageInput.files.length == 0) {
        errors.value = "Nous avons besoin d'une image pour faire la recherche"
    } else {
        formData.append(`image`, imageInput.files[0])

        axios
            .post(`${BASE_URL}comparedata`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    Accept: 'application/json'
                }
            })
            .then((response) => {
                console.log(response);
                
                similarity.value = response.data
            }).then(() => {
                loading.value = false
            })
            .catch((error) => {
                errors.value = error.response.data.errors
                loading.value = false
            })
    }
}

function load(data) {
    let newData = JSON.stringify(data)
    let link = document.createElement('a')
    let url = new Blob([newData])

    link.href = URL.createObjectURL(url)
    link.setAttribute('download', 'data.txt')
    link.click()

    document.removeChild(link)
}

function clear() {
    imageSrc.value = []
    selectedFiles.value = []
    similarity.value = null
}
</script>
