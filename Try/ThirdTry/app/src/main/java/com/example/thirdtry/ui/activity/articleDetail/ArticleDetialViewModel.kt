package com.example.thirdtry.ui.activity.articleDetail

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.thirdtry.api.RetrofitClient
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.base.BaseResult
import com.example.thirdtry.model.Article
import com.example.thirdtry.model.ArticleDetail
import com.example.thirdtry.model.Good

class ArticleDetialViewModel: ViewModel() {
    lateinit var token: String
    fun getArticleDetail(token: String, id: String): MutableLiveData<BaseDataResult<ArticleDetail>> =
        RetrofitClient.serviceApi.getArticleDetail("JWT $token", id)
    fun fav(token: String, articleID: Int) : MutableLiveData<BaseResult> =
        RetrofitClient.serviceApi.fav("JWT $token", articleID)

    fun comment(token: String, articleID: Int, content : String) : MutableLiveData<BaseResult> =
        RetrofitClient.serviceApi.comment("JWT $token", articleID, content)
}