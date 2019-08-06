from graphene_django import DjangoObjectType
import graphene
from cms.models import * 
class Courses(DjangoObjectType):
    class Meta:
        model = Course

class Lessons(DjangoObjectType):
    class Meta:
        model = Lesson



class Chapters(DjangoObjectType):
    class Meta:
        model = Chapter



class Categories(DjangoObjectType):
    class Meta:
        model = Category 


class Subcategories(DjangoObjectType):
    class Meta:
        model = Subcategory                        



class Query(graphene.ObjectType):
	courses = graphene.List(Courses)
	categories = graphene.List(Categories)
	subcategories = graphene.List(Subcategories)
	chapters = graphene.List(Chapters)
	lessons = graphene.List(Lessons)


	def resolve_courses(self, info):
	    return Course.objects.all()

	def resolve_categories (self, info):
	    return Categories.objects.all()    

	def resolve_chapter(self, info):
	    return Chapter.objects.all()    
	def resolve_lesson(self, info):
			return Lessons.objects.all()    

	def resolve_subcategories (self, info):
	    return Subcategories.objects.all()        

schema = graphene.Schema(query=Query)