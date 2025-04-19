<script setup lang="ts">
import { ref } from 'vue'
import { useMotion } from '@vueuse/motion'
import { uploadFile } from '@/utils/api'

const fileInput = ref<HTMLInputElement | null>(null)
const files = ref<File[]>([])
const status = ref<'idle' | 'success' | 'error' | 'uploading'>('idle')

function triggerInput() {
  fileInput.value?.click()
}

function handleChange(e: Event) {
  const fileList = (e.target as HTMLInputElement).files
  if (fileList && fileList[0]) {
    files.value = Array.from(fileList)
  }
}

async function upload() {
  if (!files.value.length) return
  status.value = 'uploading'
  const formData = new FormData()
  formData.append('file', files.value[0])
  formData.append('user_id', 'karna23')
  
  try {
    await uploadFile(files.value[0], 'karna23')
    status.value = 'success'
  } catch {
    const message = await error?.response?.json?.() || error?.message;

    if (message?.error === "File is not syllabus content.") {
      status.value = "invalid";
    } else {
      status.value = "error";
    }
  }
}
</script>

<template>
  <div
    class="w-full max-w-4xl mx-auto min-h-96 border border-dashed bg-white dark:bg-black border-neutral-200 dark:border-neutral-800 rounded-lg"
  >
    <div
      class="p-10 group cursor-pointer w-full relative overflow-hidden"
      @click="triggerInput"
    >
      <input
        ref="fileInput"
        type="file"
        class="hidden"
        @change="handleChange"
      />

      <div class="text-center space-y-2">
        <p class="font-bold text-neutral-700 dark:text-neutral-300">
          Upload file
        </p>
        <p class="text-neutral-400 text-sm">
          Drag or drop your files here or click to upload
        </p>
      </div>

      <div v-if="files.length" class="mt-6">
        <p class="text-sm text-neutral-500">Selected: {{ files[0].name }}</p>
        <p class="text-xs text-neutral-400">
          Size: {{ (files[0].size / 1024 / 1024).toFixed(2) }} MB
        </p>
        <p class="text-xs text-neutral-400">
          Type: {{ files[0].type }}
        </p>
        <p class="text-xs text-neutral-400">
          Last Modified: {{ new Date(files[0].lastModified).toLocaleDateString() }}
        </p>
      </div>

      <div v-if="status === 'uploading'" class="mt-4 text-blue-500 text-sm">Uploading...</div>
      <div v-if="status === 'success'" class="mt-4 text-green-500 text-sm">Upload successful!</div>
      <div v-if="status === 'error'" class="mt-4 text-red-500 text-sm">Upload failed. Try again.</div>

      <div class="mt-6">
        <button
          @click.stop="upload"
          class="bg-black text-white px-4 py-2 rounded hover:bg-neutral-800 transition"
        >
          Upload
        </button>
      </div>
    </div>
  </div>
</template>
