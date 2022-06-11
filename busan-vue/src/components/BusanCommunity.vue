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
            <h2 class="text-center">커뮤니티</h2>
            <div style="float:right" class="my-3">
                <router-link to="/communityinsertform"><input class="btn btn-outline-secondary btn-sm" type="button" value="커뮤니티 작성"></router-link>
            </div>
            <br/>
            <table class="table table-light table-hover">
                <thead>
                    <tr>
                        <th>번호</th>
                        <th>제목</th>
                        <th>작성자</th>
                        <th>작성일자</th>
                        <th>조회수</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>
                            <router-link to="/communitydetail">2022.6.6.(월) 현충일 정기휴무일 변경 안내</router-link>
                        </td>
                        <td>부산관광공사</td>
                        <td>2022-05-30</td>
                        <td>21</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>
                            <a href="">사회적거리두기에 따른 사업장 운영시간 변경 안내(2022.4.18.~)</a>
                        </td>
                        <td>관광사업팀</td>
                        <td>2022-04-18</td>
                        <td>198</td>
                    </tr>
                </tbody>
            </table>
            <div style="clear:both;">
                <form class="row g-3 align-items-center" action="" method="get"> 
                    <div class="col-auto">
                    <select class="form-select" name="condition" id="condition">
                        <option value="title_content" >제목+내용</option>
                        <option value="title" >제목</option>
                        <option value="writer" >작성자</option>
                    </select>
                    </div>
                    <div class="col-auto">
                        <input class="form-control" type="text" id="keyword" name="keyword" placeholder="검색어를 입력하세요" value=""/>
                    </div>
                    <div class="col-auto">
                        <button class="btn btn-outline-secondary " type="submit">검색</button>
                    </div>
                </form>	
                <br>
                <p>
                    전체 <strong>?</strong> 개의 글이 검색 되었습니다.
                </p>
            </div>
            <nav>
                <ul class="pagination justify-content-center">
                    <li class="page-item">
                        <a class="page-link" href="">Prev</a>
                    </li>
                    <li class="page-item active">
                        <a class="page-link" href="">1</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="">Next</a>
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
.page-ui ul{
    list-style-type: none;
    padding: 0;
}

.page-ui ul > li{
    float: left;
    padding: 5px;
}

a { 
text-decoration:none;
color:black;
} 
</style>