#!/usr/bin/env ruby

# Class definition.
class Greeter
  def initialize(name = "World")
    @name = name
  end

  def say_hi
    puts "Hello, #{@name}!"
  end

  def say_bye
    puts "Goodbye, #{@name}!"
  end
end

# Instantiation and execution.
g = Greeter.new("User")
g.say_hi
g.say_bye

# Getting instance methods of the Greeter class.
puts("Instance methods defined for Greeter:")
puts(Greeter.instance_methods)
puts()

# Getting only instance methods defined during class definition.
puts("Instance methods defined at Greeter level:")
puts(Greeter.instance_methods(false))
puts()

# Can check which methods the instance will 'respond' to.
puts("Reponds to name method?:"+g.respond_to?("name").to_s)
puts("Responds to say_hi method?:"+g.respond_to?("say_hi").to_s)
puts("Responds to to_s method?:"+g.respond_to?("to_s").to_s)
puts()

# Now, open up the class again and modify it to give access to name.
class Greeter
  attr_accessor:name
end

puts("Responds to name method?:"+g.respond_to?("name").to_s)

g.say_hi
g.name = "Betty"
g.say_hi
