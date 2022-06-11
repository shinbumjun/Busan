<template>
  <main>
    <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="https://cdn.pixabay.com/photo/2020/03/12/14/24/busan-4925217_1280.jpg" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>커뮤니티</p>
                            <p style="font-size: 30px;">community</p>
                        </div>
                    </div>
                </div>
            </div>
    </div>
    <div class="box" style="height: 1000px;">
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
    </div>
  </main>
</template>

<script>
export default {
}
</script>

<style>
  textarea {
    height: 20em;
  }
</style>