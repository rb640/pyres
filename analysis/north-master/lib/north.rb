require 'compass'
require 'sassy-maps'

base_directory  = File.join(File.dirname(__FILE__), '..')
stylesheets_dir = File.join(base_directory, 'north')
Compass::Frameworks.register("north", :path => base_directory, :stylesheets_directory => stylesheets_dir)

module North
  VERSION = "0.2.0"
  DATE = "2014-02-17"
end