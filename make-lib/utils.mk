define check-var
ifndef $(1)
$$(error <$(1)> is a required variable!)
endif
endef

manage: ## Run Django manage.py tools
	$(eval $(call check-var,C))
	@poetry run reseller_cashback/manage.py $(C)
