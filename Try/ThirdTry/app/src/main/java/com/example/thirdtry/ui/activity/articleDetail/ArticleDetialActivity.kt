package com.example.thirdtry.ui.activity.articleDetail

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.thirdtry.R
import org.greenrobot.eventbus.EventBus
import org.greenrobot.eventbus.ThreadMode
import org.greenrobot.eventbus.Subscribe
import android.view.View
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.databinding.ActivityArticleDetialBinding
import com.example.thirdtry.model.ArticleDetail
import kotlinx.android.synthetic.main.activity_article_detial.*
import kotlinx.android.synthetic.main.activity_article_detial.spin_kit



class ArticleDetialActivity : AppCompatActivity() {
    companion object {
        lateinit var instance: ArticleDetialActivity
    }
    private val adapter: ArticleDetialBindingAdapter by lazy {
        ArticleDetialBindingAdapter(articleDetail, viewModel)
    }
    private var id: String? = null
    private lateinit var viewModel: ArticleDetialViewModel
    private lateinit var token: String
    private lateinit var binding: ActivityArticleDetialBinding
    private lateinit var articleDetail: ArticleDetail

    private val mObserver: Observer<BaseDataResult<ArticleDetail>> by lazy {
        Observer<BaseDataResult<ArticleDetail>> {
            if (it == null) {
                Toast.makeText(this, "网络开小差了，请稍后", Toast.LENGTH_SHORT).show()
                return@Observer
            } else if(!this::articleDetail.isInitialized) {
                articleDetail = it.subjects
                rv.adapter = adapter
                adapter.notifyDataSetChanged()
                spin_kit.visibility = View.GONE
            } else{
                articleDetail.comments.clear()
                articleDetail.comments.addAll(it.subjects.comments)
                adapter.notifyDataSetChanged()
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_article_detial)
        EventBus.getDefault().register(this)
        instance = this
        binding = DataBindingUtil.setContentView(this, R.layout.activity_article_detial)
        val layoutManager = LinearLayoutManager(this)
        layoutManager.orientation = LinearLayoutManager.VERTICAL
        rv.layoutManager=layoutManager
    }

    @Subscribe(threadMode = ThreadMode.MAIN, sticky = true)
    fun onMessageEvent(event: String) {
        this.id = event
        viewModel = ViewModelProviders.of(this).get(ArticleDetialViewModel::class.java)
        val s = getSharedPreferences("loginToken", Context.MODE_PRIVATE)
        token = s.getString("token", "")!!
        viewModel.token = token
        getData()
    }
    fun getData(){
        viewModel.getArticleDetail(token, this.id!!).observe(this, mObserver)
    }
}
