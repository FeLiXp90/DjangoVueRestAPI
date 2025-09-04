<template>
  <div v-if="post" class="p-6 max-w-3xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900">{{ post.titulo }}</h1>

    <!-- Exibir imagem, se existir -->
    <img
      v-if="post.thumbnail"
      :src="'http://127.0.0.1:8000' + post.thumbnail"
      :alt="post.titulo"
      class="w-full h-64 object-cover my-4 rounded"
    >

    <!-- Conteúdo do post -->
    <div class="text-gray-800 whitespace-pre-line">
        
        {{ post.conteudo }}</div>
  </div>
  <div v-else class="p-6 text-center">
    Carregando...
  </div>
</template>

<script>
import { getAPI } from '../axios-api' //aqui recebe o json

export default {
  name: 'PostDetail',
  data() {
    return {
      post: null
    }
  },
  async created() {
    const slug = this.$route.params.slug
    try {
      const response = await getAPI.get(`/meusite/post/${slug}/`)
      this.post = response.data
    } catch (error) {
      console.error('Erro ao carregar post:', error)
      this.post = null
    }
  }
}
</script>