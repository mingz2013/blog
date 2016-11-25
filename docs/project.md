- 新建项目 mingz2013.github.io.src
`git clone https://github.com/mingz2013/mingz2013.github.io.src.git`
`cd mingz2013.github.io.src`
- 添加子模块 到目录output
`git submodule add https://github.com/mingz2013/mingz2013.github.io.git output`

- 初始化pelican项目
`pelican-quickstart`


- vim publishconf.py

	    DELETE_OUTPUT_DIRECTORY = True # 删除output文件夹， 切记，一定先注释掉此处，否则会删除.git,下面的命令执行不成功，我在这里因为这个搞了很久


- vim Makefile

		clean:
		   # [ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
		   rm -rf $(OUTPUTDIR)/*  # 避免删除.git
		
		github: publish
			# ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
			# git push origin $(GITHUB_PAGES_BRANCH)
			cd $(OUTPUTDIR); git add .; git commit -m "update web site"; git push origin master
			cd $(BASEDIR); git add .; git commit -m "update web site"; git push origin master


- 执行命令
`make github`

