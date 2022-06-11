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
            <a href=""><input class="btn btn-outline-secondary btn-sm" type="button" value="수정"></a>
            <a href=""><input class="btn btn-outline-secondary btn-sm" type="button" value="삭제"></a>
        </div>
        <br>
        <br>
        <table class="table table-striped">
            <tbody>
                <tr>
                    <th>번호</th>
                    <td>1</td>
                </tr>
                <tr>
                    <th>작성자</th>
                    <td>부산관광공사</td>
                </tr>
                <tr>
                    <th>제목</th>
                    <td>낙동강생태탐방선 운항 임시 중단 안내</td>
                </tr>
                <tr>
                    <th>내용</th>
                    <td colspan="2">
                        <div class="content">코로나19 확산 방지 및 방역 수칙에 따라 낙동강생태탐방선 운항을 임시 중단합니다.
                            <br><br>
                            중단기간: 2월24일(목) ~ 2월27일(일) 4일간
                        </div>
                    </td>
                </tr>
                <tr>
                    <th>조회수</th>
                    <td>21</td>
                </tr>
                <tr>
                    <th>작성일자</th>
                    <td>2022-05-30</td>
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
export default {

}
</script>

<style>

</style>