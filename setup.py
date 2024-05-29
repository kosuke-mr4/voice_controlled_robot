from setuptools import setup, find_packages

setup(
    name='voice_controlled_robot',
    version='0.0.0', 
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'rospy',
        'std_msgs',
        'geometry_msgs',
        'sensor_msgs',
    ],
    include_package_data=True,
    description='A voice controlled robot package for ROS',
    author='murakami-k',
    author_email='murakami-k@todo.todo',
    license='TODO',
    zip_safe=False,
)

