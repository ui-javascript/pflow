<template>
  <div id="vditor" style="margin: 10px 0"></div>
</template>

<script setup>
import {ref, nextTick, onMounted} from "vue";
import Vditor from "vditor";
import "vditor/dist/index.css"

let editor = ref(null);

let toolbar = [
  'emoji',
  'headings',
  'bold',
  'italic',
  'strike',
  'link',
  '|',
  'list',
  'ordered-list',
  'check',
  'outdent',
  'indent',
  '|',
  'quote',
  'line',
  'code',
  'inline-code',
  'insert-before',
  'insert-after',
  '|',
  'upload',
  // 'record',
  'table',
  '|',
  'undo',
  'redo',
  '|',
  'edit-mode',
  // 'content-theme',
  // 'code-theme',
  'export',
  {
    name: 'more',
    toolbar: [
      'fullscreen',
      'both',
      'preview',
      // 'info',
      // 'help',
    ],
  }]


onMounted(() => {

  editor = new Vditor('vditor', {
    mode: 'wysiwyg',
    height: 500,
    outline: {
      enable: true,
      position: 'right',
    },
    debugger: true,
    typewriterMode: true,
    preview: {
      markdown: {
        toc: true,
        mark: true,
        footnotes: true,
        autoSpace: true,
      },
      math: {
        engine: 'KaTeX',
      },
    },
    toolbarConfig: {
      // pin: true,
    },
    counter: {
      enable: true,
      type: 'text',
    },
    toolbar,

  })

  // @fix
  nextTick(() => {
    // code.value = "xxx"
    // code.value = "def factorial(num):\n\tfact=1\tfor i in range(1,num+1):\n\t\tfact = fact*i\n\treturn fact\nprint(factorial(5))"
  })

})

</script>