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
        <br/>
        <h2 class="text-center">커뮤니티 상세페이지</h2>
        <br>
        <div style="float:right">
            <router-link to="/community"><input class="btn btn-outline-secondary btn-sm" type="button" value="목록"></router-link>
            <router-link to="/communityinsertform"><input class="btn btn-outline-secondary btn-sm" type="button" value="수정"></router-link>
            <input class="btn btn-outline-secondary btn-sm" type="button" value="삭제" @click="delPosts()">
        </div>
        <br>
        <br>
        <table class="table table-striped">
            <tbody>
                <tr>
                    <th>번호</th>
                    <td>{{items.id}}</td>
                </tr>
                <tr>
                    <th>작성자</th>
                    <td>{{items.author_name}}</td>
                </tr>
                <tr>
                    <th>제목</th>
                    <td>{{items.title}}</td>
                </tr>
                <tr>
                    <th>내용</th>
                    <td colspan="2">
                        <div class="content">{{items.content}}<br><br></div>
                    </td>
                </tr>
                <tr>
                    <th>조회수</th>
                    <td>{{items.readcnt}}</td>
                </tr>
                <tr>
                    <th>작성일자</th>
                    <td>{{items.dt_created}}</td>
                </tr>
            </tbody>
        </table>
        <br>
        <nav>
            <ul class="pagination justify-content-center">
                <li class="page-item mr-3">
                    <a class="page-link" href="">&larr; Prev</a>
                </li>
                <li class="page-item">
                    <a class="page-link" href="">Next &rarr;</a>
                </li>
            </ul>
        </nav> 
    </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
 data() {
     return {
         items: []
     }
 },
 created(){
     axios.get(`/api/v1/board/${this.$route.params.id}/`)
     .then((response) => this.items = response.data)
     .catch((err) => console.log(err))
 },
 methods: {
    delPosts() {
      axios.delete(`/api/v1/board/${this.$route.params.id}/`, {headers: { 'content-type':
      'application/json',
      // 나중에 받아올 토큰값을 적는다. 현재 임시로 test3의 토큰값을 적어놓음.
      'Authorization': 'token e3594ca771f406537f201cda58706c0cdd773249cd98bc213d4dd746726245e7' 
      }})
      .then(res => {
        console.log(res.data)
        alert("성공적으로 삭제되었습니다.")
        this.$router.push("/community")
      }).catch(e => {
        alert(e.response.data)
      })
    },
 }
}
</script>

<style>

</style>