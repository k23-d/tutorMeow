<template>
  <div
    class="w-full max-w-4xl mx-auto min-h-96 border border-dashed bg-white dark:bg-black border-neutral-200 dark:border-neutral-800 rounded-lg"
    @click="triggerFile"
  >
    <input
      ref="fileInput"
      type="file"
      class="hidden"
      @change="handleChange"
    />
    <div class="text-center p-10">
      <p class="font-bold text-neutral-700 dark:text-neutral-300">Upload file</p>
      <p class="text-neutral-400 mt-2">Drag or drop your files here or click to upload</p>
      <div class="mt-6" v-if="files.length">
        <div
          v-for="(file, i) in files"
          :key="i"
          class="p-4 mt-4 rounded-md bg-white dark:bg-neutral-900 shadow-sm"
        >
          <p class="truncate max-w-xs text-neutral-700 dark:text-neutral-300">{{ file.name }}</p>
          <p class="text-sm text-neutral-600 dark:text-white">{{ (file.size / 1024 / 1024).toFixed(2) }} MB</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const fileInput = ref<HTMLInputElement | null>(null);
const files = ref<File[]>([]);

const triggerFile = () => {
  fileInput.value?.click();
};

const handleChange = (e: Event) => {
  const input = e.target as HTMLInputElement;
  if (input.files) {
    files.value = Array.from(input.files);
    console.log('Uploaded files:', files.value);
    // TODO: send to backend via axios or fetch
  }
};
</script>
