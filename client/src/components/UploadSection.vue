<script setup lang="ts">
import FileUpload from '@/components/ui/FileUpload.vue'
</script>

<template>
  <div class="p-4">
    <FileUpload @change="handleFileUpload" />
  </div>
</template>
