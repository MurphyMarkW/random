#!/usr/bin/env ruby

# Class definition.
class MegaGreeter
  attr_accessor:names

  def initialize(names = "World")
    @names = names
  end

  def say_hi
    if @names.nil? then
      puts "..."
    elsif @names.respond_to?("each") then
      # @names is a list. Will iterate.
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      # @names is not a list.
      puts "Hello #{@names}!"
    end
  end

  def say_bye
    if @names.nil? then
      puts "..."
    elsif @names.respond_to?("join")
      # @names is a list. Will join.
      puts "Goodbye #{@names.join(", ")}."
    else
      # @names is not a list.
      puts "Goodbye #{@names}."
    end
  end
end

if __FILE__ == $0
  mg = MegaGreeter.new
  mg.say_hi
  mg.say_bye

  # Change names to be "User"
  mg.names = "User"
  mg.say_hi
  mg.say_bye

  # Change names to a list.
  mg.names = ['Alberto','Roberto','Mr. Roboto']
  mg.say_hi
  mg.say_bye

  # Change names to nil.
  mg.names = nil
  mg.say_hi
  mg.say_bye
end
