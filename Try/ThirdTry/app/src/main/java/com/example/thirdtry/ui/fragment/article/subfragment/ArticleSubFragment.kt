package com.example.thirdtry.ui.fragment.article.subfragment

import android.content.SharedPreferences
import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import android.os.Handler
import android.view.View
import android.widget.Toast
import androidx.lifecycle.Observer
import androidx.recyclerview.widget.LinearLayoutManager


import com.example.thirdtry.R
import com.example.thirdtry.base.BaseDataResult
import com.example.thirdtry.base.BaseFragment
import com.example.thirdtry.model.Article
import com.example.thirdtry.ui.fragment.article.ArticleBindingAdapter
import com.example.thirdtry.ui.fragment.article.ArticleViewModel
import kotlinx.android.synthetic.main.article_fragment.*
import kotlinx.android.synthetic.main.article_subfragment.*
import org.greenrobot.eventbus.Subscribe
import org.greenrobot.eventbus.ThreadMode


private const val ARG_PARAM1 = "0"
class ArticleSubFragment : BaseFragment() {
    private lateinit var viewModel: ArticleViewModel
    private var articles = mutableListOf<Article>()
    private val adapter: ArticleBindingAdapter by lazy {
        ArticleBindingAdapter(articles)
    }
    companion object {
        @JvmStatic
        fun newInstance(param1: Int) =
            ArticleSubFragment().apply {
                arguments = Bundle().apply {
                    putInt(ARG_PARAM1, param1)
                }
            }
    }

    private var type: Int? = null

    override fun getLayoutId(): Int = R.layout.article_subfragment

    private val mObserver1: Observer<BaseDataResult<MutableList<Article>>> by lazy {
        Observer<BaseDataResult<MutableList<Article>>> {
            if (it == null){
                Toast.makeText(activity, "无网络连接", Toast.LENGTH_SHORT).show()
                return@Observer
            }
            else{
                if (articles.isEmpty()) {
                    try{
                        this.articles.addAll(it.subjects)
                        adapter.notifyDataSetChanged()
                        spin_kit.visibility = View.GONE
                    }finally { }
                }
                else{
                    this.articles.clear()
                    this.articles.addAll(it.subjects)
                    adapter.notifyDataSetChanged()
                }
            }
        }
    }
    private val mObserver: Observer<MutableList<Article>> by lazy {
        Observer<MutableList<Article>> {
            if (it == null){
                Toast.makeText(activity, "无网络连接", Toast.LENGTH_SHORT).show()
                return@Observer
            }
            else{
                if (articles.isEmpty()) {
                    try{
                        this.articles.addAll(it)
                        adapter.notifyDataSetChanged()
                        spin_kit.visibility = View.GONE
                    }finally { }
                }
                else{
                    this.articles.clear()
                    this.articles.addAll(it)
                    adapter.notifyDataSetChanged()
                }
            }
        }
    }


    override fun initView() {
        arguments?.let {
            type = it.getInt(ARG_PARAM1)
        }
        line_recy_view.layoutManager = LinearLayoutManager(this.context)
        line_recy_view.adapter = adapter
        SRL.setOnRefreshListener {
            when(type){
                0-> viewModel.getArticles(token).observe(this, mObserver1)
                1->viewModel.getArticlesByType(token,"sqz").observe(this, mObserver)
                3->viewModel.getArticlesByType(token,"poor_sleep").observe(this, mObserver)
                4->viewModel.getArticlesByType(token,"low_dkl").observe(this, mObserver)
                2->viewModel.getArticlesByType(token,"little_hair").observe(this, mObserver)
            }
            //下拉刷新图标持续时间
            Handler().postDelayed({
                if (SRL.isRefreshing) {
                    SRL.isRefreshing = false
                }
            }, 750)
        }

    }

    override fun initViewModel() {
        viewModel = ViewModelProviders.of(this.activity!!).get(ArticleViewModel::class.java)
        when(type){
            0-> viewModel.getArticles(token).observe(this, mObserver1)
            1->viewModel.getArticlesByType(token,"sqz").observe(this, mObserver)
            3->viewModel.getArticlesByType(token,"poor_sleep").observe(this, mObserver)
            4->viewModel.getArticlesByType(token,"low_dkl").observe(this, mObserver)
            2->viewModel.getArticlesByType(token,"little_hair").observe(this, mObserver)
        }


    }


}
