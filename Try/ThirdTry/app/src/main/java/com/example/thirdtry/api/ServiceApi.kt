package com.example.thirdtry.api

import androidx.lifecycle.MutableLiveData
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.base.BaseResult
import com.example.thirdtry.model.*
import com.example.thirdtry.ui.activity.login.LoginModel
import retrofit2.http.*
import java.util.*


interface ServiceApi {
    @POST("/jwt-token-auth/")
    @FormUrlEncoded
    fun login(@Field("username") username: String, @Field("password") password: String):
            MutableLiveData<BaseDataResult<LoginModel>>

    @POST("/jwt-token-refresh/")
    @FormUrlEncoded
    fun refresh_login(@Field("token") token: String):
            MutableLiveData<BaseDataResult<LoginModel>>

    @POST("/api/verify/")
    @FormUrlEncoded
    fun verify(@Field("email") email: String):
            MutableLiveData<BaseResult>

    @POST("/api/user/")
    @FormUrlEncoded
    fun register(
        @Field("name") name: String, @Field("password") password: String,
        @Field("email") email: String, @Field("code") code: String, @Field("gender") gender: String,
        @Field("birthday") birthday: String, @Field("typ") type: String
    ): MutableLiveData<BaseResult>

    @GET("/api/articles/")
    fun getArticles(@Header("Authorization") Authorization: String): MutableLiveData<BaseDataResult<MutableList<Article>>>

    @GET("/api/articles_type/")
    fun getArticlesByType(@Header("Authorization") Authorization: String, @Query("typ") typ: String): MutableLiveData<MutableList<Article>>

    @GET("/api/articles/{id}/")
    fun getArticleDetail(@Header("Authorization") Authorization: String, @Path("id") Id: String)
            : MutableLiveData<BaseDataResult<ArticleDetail>>

    @GET("/api/history/")
    fun getHistory(@Header("Authorization") Authorization: String): MutableLiveData<BaseDataResult<MutableList<Record>>>

    @GET("/api/fav/")
    fun getFav(@Header("Authorization") Authorization: String): MutableLiveData<BaseDataResult<MutableList<Record>>>

    @POST("/api/fav/")
    @FormUrlEncoded
    fun fav(@Header("Authorization") Authorization: String, @Field("article") Article: Int): MutableLiveData<BaseResult>

    @POST("/api/comment/")
    @FormUrlEncoded
    fun comment(
        @Header("Authorization") Authorization: String, @Field("article") Article: Int, @Field(
            "content"
        ) Content: String
    ): MutableLiveData<BaseResult>

    @GET("/api/comment/")
    fun getComment(@Header("Authorization") Authorization: String): MutableLiveData<BaseDataResult<MutableList<Comment>>>

    @GET("/api/goods/")
    fun getGoods(@Header("Authorization") Authorization: String): MutableLiveData<BaseDataResult<MutableList<Good>>>

    @GET("/api/goods/{id}/")
    fun getGoodDetail(@Header("Authorization") Authorization: String, @Path("id") Id: String)
            : MutableLiveData<Good>

    @GET("/api/scheme/")
    fun getScheme(@Header("Authorization") Authorization: String)
            : MutableLiveData<BaseDataResult<Scheme>>


    @PUT("/api/user/{id}/")
    @FormUrlEncoded
    fun editInformation(
        @Header("Authorization") Authorization: String, @Path("id") Id: String,
        @Field("name") name: String, @Field("gender") gender: String,
        @Field("birthday") birthday: String, @Field("typ") type: String
    ): MutableLiveData<Information>

    @GET("/api/user/{id}/")
    fun getInformation(@Header("Authorization") Authorization: String, @Path("id") Id: String)
            : MutableLiveData<Information>

}
