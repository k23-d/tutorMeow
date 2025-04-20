<!-- components/ui/GridPattern.vue -->
<template>
  <div
    class="absolute inset-0 pointer-events-none z-0 scale-105 bg-gray-100 dark:bg-neutral-900 flex flex-wrap gap-px"
  >
    <template v-for="i in rows">
      <template v-for="j in columns">
        <div
          :key="`${i}-${j}`"
          class="w-[10px] h-[10px] shrink-0 rounded-[2px]"
          :class="(i + j) % 2 === 0
            ? 'bg-gray-50 dark:bg-neutral-950'
            : 'bg-gray-50 dark:bg-neutral-950 shadow-[0px_0px_1px_3px_rgba(255,255,255,1)_inset] dark:shadow-[0px_0px_1px_3px_rgba(0,0,0,1)_inset]'"
        />
      </template>
    </template>
  </div>
</template>

<script setup lang="ts">
const rows = 11;
const columns = 41;
</script>
