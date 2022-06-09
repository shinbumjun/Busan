<template>
  <main>
      <div class="container">
        <br>
        <h2 class="text-center">커뮤니티 작성</h2>
        <form action="" method="post" id="insertForm">
            <div class="mb-3">
                <label class="form-label" for="title">제목</label>
                <input class="form-control" type="text" name="title" id="title"/>
            </div>
            <div class="mb-3">
                <label class="form-label" for="content">내용</label> 
                <textarea class="form-control"  name="content" id="content"></textarea>
            </div>
            <button class="btn btn-outline-secondary btn-sm" type="submit">저장</button>
        </form>
    </div>

  </main>
</template>

<script>
export default {
}
</script>

<style>
</style>